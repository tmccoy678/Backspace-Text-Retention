use std::cell::RefCell;
use std::fmt::Write;

const ERASE: [u8; 3] = [0x08, 0x20, 0x08];
const CHILD_MARKER: &str = "\r\n\r\nCHILD PROCESS RECEIVED ONLY:\r\n";

#[derive(Debug, Clone)]
struct State {
    visible: String,
    committed: Option<String>,
    bytes: Vec<u8>,
    composition_end: Option<usize>,
}

impl Default for State {
    fn default() -> Self {
        Self {
            visible: String::new(),
            committed: None,
            bytes: b"> ".to_vec(),
            composition_end: None,
        }
    }
}

impl State {
    fn type_character(&mut self, codepoint: u32) {
        if self.committed.is_some() {
            return;
        }
        let Some(character) = char::from_u32(codepoint) else {
            return;
        };
        if !matches!(character, ' '..='~') {
            return;
        }
        self.visible.push(character);
        let mut buffer = [0; 4];
        self.bytes
            .extend_from_slice(character.encode_utf8(&mut buffer).as_bytes());
    }

    fn backspace(&mut self) -> bool {
        if self.committed.is_some() || self.visible.pop().is_none() {
            return false;
        }
        self.bytes.extend_from_slice(&ERASE);
        true
    }

    fn commit(&mut self) {
        if self.committed.is_some() {
            return;
        }
        self.committed = Some(self.visible.clone());
        self.bytes.extend_from_slice(b"\r\n");
        self.composition_end = Some(self.bytes.len());
        self.bytes.extend_from_slice(CHILD_MARKER.as_bytes());
        self.bytes.extend_from_slice(b"<");
        self.bytes.extend_from_slice(self.visible.as_bytes());
        self.bytes.extend_from_slice(b">\r\n");
    }

    fn composition(&self) -> &[u8] {
        &self.bytes[..self.composition_end.unwrap_or(self.bytes.len())]
    }

    fn erase_runs(&self) -> Vec<usize> {
        erase_runs(self.composition())
    }

    fn compressed(&self) -> String {
        compressed(self.composition())
    }

    fn hex_dump(&self) -> String {
        hex_dump(&self.bytes)
    }

    fn report(&self) -> String {
        let runs = self.erase_runs();
        let total: usize = runs.iter().sum();
        format!(
            "RECORDER-RETAINED COMPOSITION HISTORY\n{}\n\nVISUAL-ERASE RUNS: {}\nTOTAL 08 20 08 TRIPLETS: {}\n\nCHILD PROCESS RECEIVED ONLY\n<{}>\n\nRAW BYTE TRANSCRIPT\n{}",
            self.compressed(),
            if runs.is_empty() {
                "none detected".into()
            } else {
                runs.iter()
                    .map(usize::to_string)
                    .collect::<Vec<_>>()
                    .join(", ")
            },
            total,
            self.committed.as_deref().unwrap_or("not committed"),
            self.hex_dump()
        )
    }
}

fn erase_runs(data: &[u8]) -> Vec<usize> {
    let mut runs = Vec::new();
    let mut index = 0;
    while index < data.len() {
        if !data[index..].starts_with(&ERASE) {
            index += 1;
            continue;
        }
        let mut count = 0;
        while data[index..].starts_with(&ERASE) {
            count += 1;
            index += ERASE.len();
        }
        runs.push(count);
    }
    runs
}

fn compressed(data: &[u8]) -> String {
    let mut output = String::new();
    let mut index = 0;
    while index < data.len() {
        if data[index..].starts_with(&ERASE) {
            let mut count = 0;
            while data[index..].starts_with(&ERASE) {
                count += 1;
                index += ERASE.len();
            }
            let _ = write!(output, "[08 20 08 × {count}]");
            continue;
        }
        let byte = data[index];
        index += 1;
        match byte {
            b'\r' | b'\n' => output.push('\n'),
            0x20..=0x7e => output.push(byte as char),
            _ => {
                let _ = write!(output, "\\x{byte:02x}");
            }
        }
    }
    output.trim_end().to_string()
}

fn hex_dump(data: &[u8]) -> String {
    let mut output = String::new();
    for (row, chunk) in data.chunks(16).enumerate() {
        let _ = write!(output, "{:08x}  ", row * 16);
        for index in 0..16 {
            if let Some(byte) = chunk.get(index) {
                let _ = write!(output, "{byte:02x} ");
            } else {
                output.push_str("   ");
            }
        }
        output.push_str(" |");
        for byte in chunk {
            output.push(if (0x20..0x7f).contains(byte) {
                *byte as char
            } else {
                '.'
            });
        }
        output.push_str("|\n");
    }
    output.trim_end().to_string()
}

thread_local! {
    static STATE: RefCell<State> = RefCell::new(State::default());
    static OUTPUT: RefCell<Vec<u8>> = const { RefCell::new(Vec::new()) };
}

fn render(kind: u32) -> String {
    STATE.with(|state| {
        let state = state.borrow();
        match kind {
            0 => state.visible.clone(),
            1 => state.compressed(),
            2 => state.hex_dump(),
            3 => state.report(),
            4 => state
                .erase_runs()
                .iter()
                .map(usize::to_string)
                .collect::<Vec<_>>()
                .join(","),
            5 => state.committed.clone().unwrap_or_default(),
            _ => String::new(),
        }
    })
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_reset() {
    STATE.with(|state| *state.borrow_mut() = State::default());
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_type(codepoint: u32) {
    STATE.with(|state| state.borrow_mut().type_character(codepoint));
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_backspace() -> u32 {
    STATE.with(|state| state.borrow_mut().backspace() as u32)
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_commit() {
    STATE.with(|state| state.borrow_mut().commit());
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_is_committed() -> u32 {
    STATE.with(|state| state.borrow().committed.is_some() as u32)
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_render(kind: u32) {
    let rendered = render(kind);
    OUTPUT.with(|output| *output.borrow_mut() = rendered.into_bytes());
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_output_ptr() -> *const u8 {
    OUTPUT.with(|output| output.borrow().as_ptr())
}

#[unsafe(no_mangle)]
pub extern "C" fn demo_output_len() -> usize {
    OUTPUT.with(|output| output.borrow().len())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn reproduces_the_live_three_run_sequence() {
        let mut state = State::default();
        for character in "Jimmy Neutrom".chars() {
            state.type_character(character as u32);
        }
        state.backspace();
        for character in "n: Boy Genius".chars() {
            state.type_character(character as u32);
        }
        for _ in 0..25 {
            state.backspace();
        }
        state.type_character('F' as u32);
        state.backspace();
        for character in "The Sims 2: Night life".chars() {
            state.type_character(character as u32);
        }
        state.commit();

        assert_eq!(state.erase_runs(), vec![1, 25, 1]);
        assert_eq!(state.committed.as_deref(), Some("The Sims 2: Night life"));
        assert!(state.report().contains("TOTAL 08 20 08 TRIPLETS: 27"));
    }

    #[test]
    fn reset_state_contains_only_the_prompt() {
        let state = State::default();
        assert_eq!(state.compressed(), ">");
        assert!(state.erase_runs().is_empty());
    }

    #[test]
    fn ignores_non_ascii_and_control_characters() {
        let mut state = State::default();
        for character in "plain 🐷 café\nnext".chars() {
            state.type_character(character as u32);
        }
        assert_eq!(state.visible, "plain  cafnext");
    }
}
