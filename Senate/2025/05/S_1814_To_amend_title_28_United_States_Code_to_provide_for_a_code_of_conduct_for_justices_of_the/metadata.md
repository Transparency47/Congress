# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1814?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1814
- Title: Supreme Court Ethics, Recusal, and Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1814
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2026-03-19T11:03:27Z
- Update date including text: 2026-03-19T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1814",
    "number": "1814",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Supreme Court Ethics, Recusal, and Transparency Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:27Z",
    "updateDateIncludingText": "2026-03-19T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2025-05-20T18:43:47Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-20T18:43:47Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "WI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "DE"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "AZ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-20",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NH"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1814is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1814\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mr. Whitehouse (for himself, Mr. Blumenthal , Ms. Baldwin , Mr. Booker , Mr. Coons , Mr. Durbin , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Sanders , Mr. Schatz , Mr. Schiff , Ms. Smith , Mr. Van Hollen , Mr. Welch , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to provide for a code of conduct for justices of the Supreme Court of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supreme Court Ethics, Recusal, and Transparency Act of 2025 .\n#### 2. Code of conduct for the Supreme Court of the United States\n##### (a) In general\nChapter 16 of title 28, United States Code, is amended by adding at the end the following:\n365. Codes of conduct (a) Justices Not later than 180 days after the date of enactment of this section, the Supreme Court of the United States shall, after appropriate public notice and opportunity for comment in accordance with section 2071, issue a code of conduct for the justices of the Supreme Court. (b) Other judges Not later than 180 days after the date of enactment of this section, the Judicial Conference of the United States shall, after appropriate public notice and opportunity for comment in accordance with section 2071, issue a code of conduct for the judges of the courts of appeals, the district courts (including bankruptcy judges and magistrate judges), and the Court of International Trade. (c) Modification The Supreme Court of the United States and the Judicial Conference may modify the applicable codes of conduct under this section after giving appropriate public notice and opportunity for comment in accordance with section 2071. 366. Public access to ethics rules The Supreme Court of the United States shall make available on its internet website, in a full-text, searchable, sortable, and downloadable format, copies of the code of conduct issued under section 365(a), any rules established by the Counselor to the Chief Justice of the United States under section 677 and any other related rules or resolutions, as determined by the Chief Justice of the United States, issued by the Counselor to the Chief Justice of the United States or agreed to by the justices of the Supreme Court. 367. Complaints against justices (a) Receipt of complaints (1) In general Not later than 180 days after the date of enactment of this section, the Supreme Court of the United States shall establish procedures, modeled after the procedures set forth in sections 351 through 364, under which individuals may file with the Court, or the Court may identify, complaints alleging that a justice of the Supreme Court\u2014 (A) has violated\u2014 (i) the code of conduct issued pursuant to section 365(a); (ii) section 455; or (iii) any other applicable provision of Federal law; or (B) has otherwise engaged in conduct that undermines the integrity of the Supreme Court. (2) Procedures Procedures established under this subsection shall, at minimum, contain provisions\u2014 (A) requiring that all complaints submitted under this section contain\u2014 (i) the signature and contact address of the complainant; (ii) a concise statement of the specific facts on which the claim of misconduct is based; and (iii) a sworn affirmation that to the best of the knowledge and belief of the complainant, under penalty of perjury, the facts alleged in the complaint are true and form a reasonable basis to believe a justice has committed misconduct under this section; and (B) providing for the restriction on the future filing of complaints with respect to complainants who are shown to have filed repetitive, harassing, or frivolous complaints, or have otherwise abused the complaint procedure. (b) Judicial investigation panel (1) In general Upon receipt or identification of a complaint under subsection (a), the Supreme Court of the United States shall refer such complaint to a judicial investigation panel, which shall be composed of a panel of 5 judges selected randomly from among the chief judge of each circuit of the United States. (2) Duties The judicial investigation panel\u2014 (A) shall review and, if appropriate as determined by the panel, investigate all complaints submitted to the panel using procedures established by the panel and modeled after the procedures set forth in sections 351 through 364; (B) shall present to the Supreme Court of the United States any findings and recommendations for necessary and appropriate action by the Supreme Court, including dismissal of the complaint, disciplinary actions, or changes to Supreme Court rules or procedures; (C) if the panel does not recommend dismissal of the complaint, not later than 30 days following the presentation of any findings and recommendations under this paragraph, shall publish a report containing such findings and recommendations; and (D) if the panel recommends dismissal of the complaint, may publish any findings and recommendations if the panel determines that such publication would be in furtherance of the public interest. (3) Powers In conducting any investigation under this section, the judicial investigation panel may hold hearings, take sworn testimony, issue subpoenas ad testificandum and subpoenas duces tecum, and make necessary and appropriate orders in the exercise of its authority. (4) Access If the judicial investigation panel determines that a substantially similar complaint was previously submitted under section 351, but that such substantially similar complaint was dismissed for lack of authority to review or act upon such complaint, the panel shall have access to any information gathered pursuant to this chapter in relation to such substantially similar complaint. (5) Compensation The judicial investigation panel may appoint and fix the compensation of such staff as it deems necessary. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 16 of title 28, United States Code, is amended by adding at the end the following:\n365. Codes of conduct. 366. Public access to ethics rules. 367. Complaints against justices. .\n#### 3. Minimum gift and disclosure standards for justices of the Supreme Court\nSection 677 of title 28, United States Code, is amended by adding at the end the following:\n(e) The Counselor, with the approval of the Chief Justice, shall establish rules governing the acceptance of gifts and the disclosure of all gifts, income, or reimbursements, as those terms are defined in section 13101 of title 5, received by any justice and any law clerk to a justice. Such rules shall, at minimum, require disclosure of any information concerning gifts, income, and reimbursements required to be disclosed under the Standing Rules of the Senate and the Rules of the House of Representatives, and restrict the acceptance of gifts, and require processes for written approval of certain gifts, to the same extent as restricted or required under the Standing Rules of the Senate and the Rules of the House of Representatives. .\n#### 4. Circumstances requiring disqualification\n##### (a) Anticorruption protections\nSubsection (b) of section 455 of title 28, United States Code, is amended by adding at the end the following:\n(6) Where the justice or judge knows that a party to the proceeding or an affiliate of a party to the proceeding made any lobbying contact, as defined in section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 ), or spent substantial funds in support of the nomination, confirmation, or appointment of the justice or judge. (7) Where the justice or judge, their spouse, their minor child, or a privately held entity owned by any such person received income, a gift, or reimbursement, as those terms are defined in section 13101 of title 5\u2014 (A) from a party to the proceeding or an affiliate of a party to the proceeding; and (B) during the period beginning on the date that is 6 years before the date on which the justice or judge was assigned to the proceeding and ending on the date of final disposition of the proceeding. .\n##### (b) Duty To know\nSubsection (c) of section 455 of title 28, United States Code, is amended to read as follows:\n(c) A justice, judge, magistrate judge, or bankruptcy judge of the United States shall ascertain\u2014 (1) the personal and fiduciary financial interests of the justice or judge; (2) the personal financial interests of the spouse and minor children residing in the household of the justice or judge; and (3) any interest of the persons described in paragraph (2) that could be substantially affected by the outcome of the proceeding. .\n##### (c) Divestment\nSubsection (f) of section 455 of title 28, United States Code, is amended by inserting under subsection (b)(4) after disqualified .\n##### (d) Duty To notify\nSection 455 of title 28, United States Code, is amended by adding at the end the following:\n(g) If at any time a justice, judge, magistrate judge, or bankruptcy judge of the United States learns of a condition that could reasonably require disqualification under this section, the justice or judge shall immediately notify all parties to the proceeding. .\n##### (e) Technical and conforming amendments\nSection 455 of title 28, United States Code, as amended by this section, is amended\u2014\n**(1)**\nin the section heading, by striking judge, or magistrate judge and inserting judge, magistrate judge, or bankruptcy judge ;\n**(2)**\nin subsection (a), by striking judge, or magistrate judge and inserting judge, magistrate judge, or bankruptcy judge ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking the judge or such lawyer and inserting the justice, the judge, or such lawyer ;\n**(B)**\nin paragraph (5)(iii), by inserting justice or before judge ; and\n**(C)**\nin paragraph (5)(iv), by inserting justice\u2019s or before judge\u2019s ;\n**(4)**\nin subsection (d)(4)(i), by inserting justice or before judge ; and\n**(5)**\nin subsection (e), by striking judge, or magistrate judge and inserting judge, magistrate judge, or bankruptcy judge of the United States .\n##### (f) Public notice\nThe rules of each court subject to section 455 of title 28, United States Code, as amended by this section, shall be amended to require that the clerk shall publish timely notice on the website of the court of\u2014\n**(1)**\nany matter in which a justice, judge, magistrate judge, or bankruptcy judge of the United States is disqualified under such section;\n**(2)**\nany matter in which the reviewing panel under section 1660 of title 28, United States Code, as added by section 5 of this Act, rules on a motion to disqualify; and\n**(3)**\nan explanation of each reason for the disqualification or ruling, which shall include a specific identification of each circumstance that resulted in such disqualification or ruling, but which shall not include any private or sensitive information deemed by a majority of the reviewing panel under section 1660 of title 28, United States Code, as added by section 5 of this Act, to be appropriate for redaction and unnecessary in order to provide the litigants and public a full understanding of the reasons for the disqualification or ruling.\n#### 5. Review of certified disqualification motions\n##### (a) In general\nChapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Review of certified motions to disqualify (a) Motion for disqualification If a justice, judge, magistrate judge, or bankruptcy judge of the United States is required to be disqualified from a proceeding under any provision of Federal law, a party to the proceeding may file a timely motion for disqualification, accompanied by a certificate of good faith and an affidavit alleging facts sufficient to show that disqualification of the justice, judge, magistrate judge, or bankruptcy judge is so required. (b) Consideration of motion A justice, judge, magistrate judge, or bankruptcy judge of the United States shall either grant or certify to a reviewing panel a timely motion filed pursuant to subsection (a) and stay the proceeding until a final determination is made with respect to the motion. (c) Reviewing panel (1) In general A reviewing panel to which a motion is certified under subsection (b) with respect to a judge, magistrate judge, or bankruptcy judge of the United States shall be composed of 3 judges selected at random from judges of the United States who do not sit on the same court\u2014 (A) as the judge, magistrate judge, or bankruptcy judge who is the subject of the motion; or (B) as the other members of the reviewing panel. (2) Circuit limitation Not more than 1 member of the reviewing panel may be a judge of the same judicial circuit as the judge, magistrate judge, or bankruptcy judge who is the subject of the motion. (3) Participation The reviewing panel, prior to its final determination with respect to a motion filed under subsection (a), shall provide the judge, magistrate judge, or bankruptcy judge of the United States who is the subject of such motion an opportunity to provide in writing the views of the judge on the motion, including the explanation of the judge for not granting the motion. (d) Supreme Court review The Supreme Court of the United States, not including the justice who is the subject of a motion seeking to disqualify a justice under subsection (a), shall be the reviewing panel for such motions. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 111 of title 28, United States Code, is amended by adding at the end the following:\n1660. Review of certified motions to disqualify. .\n#### 6. Disclosure by parties and amici\nNot later than 1 year after the date of enactment of this Act, the Supreme Court of the United States shall prescribe rules of procedure in accordance with sections 2072 through 2074 of title 28, United States Code, requiring each party or amicus to list in the petition or brief of the party or amicus, as applicable, a description and value of\u2014\n**(1)**\nany gift, income, or reimbursement, as those terms are defined in section 13101 of title 5, United States Code, provided to any justice, during the period beginning 2 years prior to the commencement of the proceeding and ending on the date of final disposition of the proceeding, by\u2014\n**(A)**\neach such party, amicus, or affiliate of each such party or amicus;\n**(B)**\nthe lawyers or law firms in the proceeding of each such party or amicus; and\n**(C)**\nthe officers, directors, or employees of each such party or amicus; and\n**(2)**\nany lobbying contact or expenditure of substantial funds by any person described in subparagraphs (A), (B), and (C) of paragraph (1) in support of the nomination, confirmation, or appointment of a justice.\n#### 7. Amicus disclosure\n##### (a) In general\nChapter 111 of title 28, United States Code, as amended by section 5, is amended by adding at the end the following:\n1661. Disclosures related to amicus activities (a) Disclosure (1) In general Any person that files an amicus brief in a court of the United States shall list in the amicus brief the name of any person who\u2014 (A) contributed to the preparation or submission of the amicus brief; (B) contributed not less than 3 percent of the gross annual revenue of the amicus, or an affiliate of the amicus, for the previous calendar year if the amicus is not an individual; or (C) contributed more than $100,000 to the amicus, or an affiliate of the amicus, in the previous calendar year. (2) Exceptions The requirements of this subsection shall not apply to amounts received in commercial transactions in the ordinary course of any trade or business by the amicus, or an affiliate of the amicus, or in the form of investments (other than investments by the principal shareholder in a limited liability corporation) in an organization if the amounts are unrelated to the amicus filing activities of the amicus. (b) Audit The Director of the Administrative Office of the United States Courts shall conduct an annual audit to ensure compliance with this section. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 111 of title 28, United States Code, as amended by section 5, is amended by adding at the end the following:\n1661. Disclosures related to amicus activities. .\n#### 8. Conflicts related to amici curiae\n##### (a) In general\nExcept as provided in subsection (b), the Supreme Court of the United States and the Judicial Conference of the United States shall prescribe rules of procedure in accordance with sections 2072 through 2074 of title 28, United States Code, for prohibiting the filing of or striking an amicus brief that would result in the disqualification of a justice, judge, or magistrate judge.\n##### (b) Initial transmittal\nThe Supreme Court of the United States shall transmit to Congress\u2014\n**(1)**\nthe proposed rules required under subsection (a) not later than 180 days after the date of enactment of this Act; and\n**(2)**\nany rules in addition to those transmitted under paragraph (1) pursuant to section 2074 of title 28, United States Code.\n#### 9. Studies and reports\n##### (a) Studies\n**(1) In general**\nNot later than the date that is 180 days after the date of enactment of this Act, and not later than December 1 of every other year thereafter, the Director of the Federal Judicial Center shall\u2014\n**(A)**\nconduct a study on the extent of compliance or noncompliance with the requirements of sections 144 and 455 of title 28, United States Code; and\n**(B)**\nsubmit to Congress the results of the study required under subparagraph (A).\n**(2) Additional time**\nWith respect to the first such study required to be submitted under paragraph (1), the requirements of that paragraph may be implemented after the date described in that paragraph if the Director of the Federal Judicial Center identifies in writing to the relevant committees of Congress the additional time needed for submission of the study.\n**(3) Facilitation of studies**\nThe Director of the Federal Judicial Center shall maintain a record of each instance in which\u2014\n**(A)**\na justice, judge, magistrate judge, or bankruptcy judge of the United States was not assigned to a case due to potential or actual conflicts; and\n**(B)**\na justice, judge, magistrate judge, or bankruptcy judge of the United States disqualifies themselves after a case assignment is made.\n##### (b) Reports to Congress\nNot later than April 1 of each year following the completion of the study required under subsection (a), the Director of the Federal Judicial Center shall submit to Congress a report containing the findings of the study and any recommendations to improve compliance with sections 144 and 455 of title 28, United States Code.\n##### (c) GAO review\n**(1) In general**\nNot later than 1 year after the date on which the report is submitted under subsection (b), if determined appropriate by the Committee on the Judiciary of the Senate or the Committee on the Judiciary of the House of Representatives, after consultation with the Comptroller General of the United States, and every 5 years thereafter, the Comptroller General of the United States shall submit to Congress a report containing\u2014\n**(A)**\nan review of the methodology and findings of the study required under subsection (a); and\n**(B)**\na review of the methodology and findings of the audit required under section 1661 of title 28, United States Code, as added by section 7 of this Act.\n**(2) Access**\nFor purposes of conducting the reviews required under paragraph (1), and consistent with section 715 of title 31, United States Code, the Comptroller General of the United States is authorized to obtain such records of the Federal Judicial Center and the Administrative Office of the United States Courts as the Comptroller requires, including those records relating to the Supreme Court of the United States.",
      "versionDate": "2025-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3513",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supreme Court Ethics, Recusal, and Transparency Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-05-30T14:17:11Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1814is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Supreme Court Ethics, Recusal, and Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supreme Court Ethics, Recusal, and Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 28, United States Code, to provide for a code of conduct for justices of the Supreme Court of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:03:34Z"
    }
  ]
}
```
