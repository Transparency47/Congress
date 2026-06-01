# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1297
- Title: Fair Day in Court for Kids Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1297
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-02-19T17:59:22Z
- Update date including text: 2026-02-19T17:59:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1297",
    "number": "1297",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Fair Day in Court for Kids Act of 2025",
    "type": "S",
    "updateDate": "2026-02-19T17:59:22Z",
    "updateDateIncludingText": "2026-02-19T17:59:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
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
        "item": {
          "date": "2025-04-03T21:37:24Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
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
      "sponsorshipDate": "2025-04-03",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
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
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
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
      "sponsorshipDate": "2025-04-03",
      "state": "CO"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
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
      "sponsorshipDate": "2025-04-03",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "GA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-03",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
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
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "OR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1297is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1297\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Ms. Hirono (for herself, Mr. Bennet , Mr. Blumenthal , Mr. Booker , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Heinrich , Mr. Hickenlooper , Mr. Kim , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mr. Murphy , Mr. Ossoff , Mr. Padilla , Mr. Sanders , Mr. Schatz , Mr. Schiff , Ms. Smith , Mr. Van Hollen , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide counsel for unaccompanied children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Day in Court for Kids Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Noncitizen**\nThe term noncitizen means an individual who is not a citizen or national of the United States.\n**(2) Unaccompanied child**\nThe term unaccompanied child has the meaning given the term unaccompanied alien child in section 462(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g) ).\n#### 3. References to aliens\nWith respect to an individual who is not a citizen or national of the United States, any reference in this Act to a noncitizen shall be deemed to refer to an individual otherwise described as an alien in any Federal law, Federal regulation, or any written instrument issued by the executive branch of the Government.\n#### 4. Improving immigration court efficiency and reducing costs by increasing access to legal information\n##### (a) Definitions\nSection 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ) is amended by adding at the end the following:\n(53) The term noncitizen means an individual who is not a citizen or national of the United States. (54) The term unaccompanied child has the meaning given the term unaccompanied alien child in section 462(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g) ). .\n##### (b) Appointment of counsel in removal proceedings; right To review certain documents in removal proceedings\nSection 240(b) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b) ) is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking under regulations of the Attorney General and inserting under regulations of the Attorney General, or in the case of an unaccompanied child, under regulations of the Secretary of Health and Human Services ;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nby striking , at no expense to the Government, ; and\n**(ii)**\nby striking the comma at the end and inserting a semicolon;\n**(C)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (D) and (E), respectively;\n**(D)**\nby inserting after subparagraph (A) the following:\n(B) the Attorney General, or in the case of an unaccompanied child, the Secretary of Health and Human Services, may appoint or provide counsel, at Government expense, to noncitizens in immigration proceedings; (C) the noncitizen, or the noncitizen\u2019s counsel, not later than 7 days after receiving a notice to appear under section 239(a), shall receive a complete copy of the noncitizen\u2019s immigration file (commonly known as an A-file ) in the possession of the Department of Homeland Security (other than documents protected from disclosure under section 552(b) of title 5, United States Code); ; and\n**(E)**\nin subparagraph (D), as redesignated, by striking , and and inserting ; and ; and\n**(2)**\nby adding at the end the following:\n(8) Failure to provide noncitizen required documents A removal proceeding may not proceed until the noncitizen, or the noncitizen\u2019s counsel if the noncitizen is represented\u2014 (A) has received the documents required under paragraph (4)(C); and (B) has been provided at least 10 days to review and assess such documents, unless the noncitizen or the noncitizen\u2019s counsel expressly waives such review period. .\n##### (c) Clarification regarding the authority of the Federal Government To appoint counsel to noncitizens in immigration proceedings\n**(1) In general**\nSection 292 of the Immigration and Nationality Act ( 8 U.S.C. 1362 ) is amended to read as follows:\n292. Right to counsel (a) In general In any removal proceeding before the Attorney General, an appeal from such a removal proceeding, and any related matter before the Department of Homeland Security or a State court, an unaccompanied child shall have the privilege of being represented by such counsel as may be authorized to practice in such proceeding or matter as he or she may choose. This subsection shall not apply to screening proceedings described in section 235(b)(1)(A). (b) Access to counsel for unaccompanied children (1) In general In any removal proceeding before the Attorney General, an appeal from such a removal proceeding, and any related matter before the Department of Homeland Security or a State court, an unaccompanied child shall be represented by counsel appointed or provided by the Secretary of Health and Human Services, at Government expense, unless the child has obtained at his or her own expense counsel authorized to practice in such proceeding or matter. (2) Timing The Secretary of Health and Human Services shall appoint or provide counsel to an unaccompanied child under paragraph (1) as expeditiously as possible after the earlier of\u2014 (A) the date on which a Notice to Appear for removal proceedings is issued to the unaccompanied child, regardless of whether the Notice to Appear has been filed with an immigration court; or (B) the date on which the unaccompanied child is placed in the custody of the Secretary of Health and Human Services. (3) Length of representation An unaccompanied child shall be represented by counsel under paragraph (1) at every stage of the proceedings, beginning with the unaccompanied child\u2019s initial appearance before an official with adjudicatory authority in removal proceedings or in related matters before the Department of Homeland Security or a State court, through the termination of immigration proceedings and resolution of any related matter before the Department of Homeland Security or a State court, even if the child attains 18 years of age or is reunified with a parent or legal guardian while the proceedings are pending. (4) Continuity in representation If counsel retained by an unaccompanied child at his or her own expense ceases representing the child for any reason, the Secretary of Health and Human Services shall ensure continued representation of the child by appointing or providing new counsel as expeditiously as possible. (5) Notice Not later than 72 hours after an unaccompanied child is taken into Federal custody, the child shall be notified that he or she will be provided with legal counsel in accordance with this subsection. (6) Within detention facilities The Secretary of Homeland Security shall ensure that unaccompanied children have access to counsel inside all detention, holding, and border facilities. (c) Pro bono representation (1) In general To the maximum extent practicable, the Secretary of Health and Human Services shall make every effort to use the services of competent counsel who agree to provide representation to such children under subsection (b) without charge to the child. (2) Development of necessary infrastructures and systems The Secretary of Health and Human Services shall establish the necessary infrastructure and systems for the appropriate identification, recruitment, training, and oversight of counsel available to provide assistance and representation to unaccompanied children under subsection (b) without charge to the child. (d) Model guidelines on legal representation of children (1) Development of guidelines The Director of the Office of Refugee Resettlement, in consultation with the Director of the Executive Office for Immigration Review, the Secretary of Homeland Security, and nongovernmental stakeholders with relevant expertise in providing immigration-related legal services to children, shall develop model guidelines for the legal representation of unaccompanied children in immigration proceedings, which shall be based on\u2014 (A) the 2018 report of the American Bar Association entitled Standards for the Custody, Placement and Care; Legal Representation; and Adjudication of Unaccompanied Alien Children in the United States ; (B) the American Bar Association Model Rules of Professional Conduct; and (C) any other source the Director of the Office of Refugee Resettlement considers appropriate. (2) Purpose of guidelines The guidelines developed under paragraph (1) shall be designed to help protect each child from any individual suspected of involvement in any criminal, harmful, or exploitative activity associated with the smuggling or trafficking of children, while ensuring the fairness of the immigration proceeding in which the child is involved. (e) Duties of counsel The duties of counsel appointed or provided under this section shall include\u2014 (1) representing the unaccompanied alien child concerned\u2014 (A) in all proceedings and matters relating to the immigration status of the child; and (B) with respect to any other action involving the Department of Homeland Security; (2) appearing in person for each of the child's\u2014 (A) individual merits hearings and master calendar hearings before the Executive Office for Immigration Review; and (B) interviews involving the Department of Homeland Security; (3) owing the same duties of undivided loyalty, confidentiality, and competent representation to the child as is due to an adult client; (4) advocating for the child\u2019s legal interests, as directed by the child\u2019s express wishes; (5) in the case of a child who does not express the objectives of representation, or is found incompetent, referring the child for the appointment of an independent child advocate, as described in section 235(c)(6) of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232(c)(6) ); and (6) carrying out other such duties as may be prescribed by the Secretary of Health and Human Services or the Director of the Executive Office for Immigration Review. (f) Savings provision Nothing in this section may be construed to supersede\u2014 (1) any duties, responsibilities, disciplinary, or ethical responsibilities an attorney may have to his or her client under State law; (2) the admission requirements under State law; or (3) any other State law pertaining to the admission to the practice of law in a particular jurisdiction. .\n**(2) Rulemaking**\nThe Secretary of Health and Human Services shall promulgate regulations to implement section 292 of the Immigration and Nationality Act, as added by paragraph (1), in accordance with the requirements set forth in section 3006A of title 18, United States Code.\n#### 5. Access by counsel to Department of Homeland Security facilities\nThe Secretary of Homeland Security shall provide access to counsel for all noncitizens detained in\u2014\n**(1)**\na facility under the supervision of U.S. Immigration and Customs Enforcement or U.S. Customs and Border Protection; or\n**(2)**\na private facility that contracts with the Department of Homeland Security to house, detain, or hold noncitizens.\n#### 6. Report on access to counsel\n##### (a) Report\nNot later than December 31 of each year, the Secretary of Health and Human Services, in consultation with the Attorney General, shall prepare and submit a report to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives regarding the extent to which the Secretary has provided counsel for unaccompanied children as described in subsection (b) of section 292 of the Immigration and Nationality Act, as amended by section 4(c).\n##### (b) Contents\nEach report submitted under paragraph (a) shall include, for the immediately preceding 1-year period\u2014\n**(1)**\nthe number and percentage of unaccompanied children described in subsection (b) of section 292 of the Immigration and Nationality Act, as amended by section 4(c), who were represented by counsel, including information specifying\u2014\n**(A)**\nthe stage of the legal process at which representation of each such child commenced;\n**(B)**\nwhether each such child was in government custody on the date on which such representation commenced; and\n**(C)**\nthe nationality and ages of such children;\n**(2)**\nthe number and percentage of children who received Know Your Rights presentations or legal screenings, including the nationality and ages of such children; and\n**(3)**\na description of the mechanisms used under subsection (b) of section 292 of the Immigration and Nationality Act, as added by section 4(c), for identifying, recruiting, and training pro bono counsel to represent unaccompanied children.\n#### 7. Motions to reopen\nSection 240(c)(7)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(c)(7)(C) ) is amended by adding at the end the following:\n(v) Special rule for unaccompanied children entitled to appointment of counsel If the Secretary of Health and Human Services fails to appoint or provide counsel for an unaccompanied child under section 292(b)\u2014 (I) the limitations under this paragraph with respect to the filing of a motion to reopen by such child shall not apply; and (II) the filing of such a motion shall stay the removal of the child. .\n#### 8. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated to the Office of Refugee Resettlement such sums as may be necessary to carry out this Act.\n##### (b) Budgetary effects\nThe budgetary effects of this Act, for the purpose of complying with the Statutory Pay-As-You-Go Act of 2010, shall be determined by reference to the latest statement titled Budgetary Effects of PAYGO Legislation for this Act, submitted for printing in the Congressional Record by the Chairman of the Senate Budget Committee, provided that such statement has been submitted prior to the vote on passage.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
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
        "name": "Immigration",
        "updateDate": "2025-05-05T12:41:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1297",
          "measure-number": "1297",
          "measure-type": "s",
          "orig-publish-date": "2025-04-03",
          "originChamber": "SENATE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1297v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fair Day in Court for Kids Act of 2025</strong></p><p>This bill provides legal protections for a <em></em>non-U.S. national (alien under federal law) who is detained or subject to immigration-related proceedings.</p><p>The Department of Justice (DOJ), or the Department of Health and Human Services (HHS) in a case involving an unaccompanied child, may appoint or provide counsel at the government's expense to non-U.S. nationals in removal proceedings and related appeals.</p><p>An unaccompanied child must be represented by counsel paid for and appointed by the government at every stage of such proceedings unless the child has obtained counsel at their own expense. If HHS fails to provide counsel to an unaccompanied child, the child's deadline for filing a motion to reopen a removal proceeding\u00a0shall not apply, and the filing of such a motion shall stay the child's removal from the United States.</p><p>The Department of Homeland Security (DHS) must provide a complete copy of a non-U.S. national's immigration file to the non-U.S. national (or the non-U.S. national's counsel) within seven days of a notice to appear for an immigration proceeding, and failure to provide the file shall result in a delay in the proceeding.</p><p>DHS must provide access to counsel for all detained non-U.S. nationals.</p><p>The Office of Refugee Resettlement must develop model guidelines for representing non-U.S. national children in immigration proceedings.</p><p>HHS must annually report on the extent to which it has provided counsel for unaccompanied children under this bill.\u00a0</p>"
        },
        "title": "Fair Day in Court for Kids Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1297.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fair Day in Court for Kids Act of 2025</strong></p><p>This bill provides legal protections for a <em></em>non-U.S. national (alien under federal law) who is detained or subject to immigration-related proceedings.</p><p>The Department of Justice (DOJ), or the Department of Health and Human Services (HHS) in a case involving an unaccompanied child, may appoint or provide counsel at the government's expense to non-U.S. nationals in removal proceedings and related appeals.</p><p>An unaccompanied child must be represented by counsel paid for and appointed by the government at every stage of such proceedings unless the child has obtained counsel at their own expense. If HHS fails to provide counsel to an unaccompanied child, the child's deadline for filing a motion to reopen a removal proceeding\u00a0shall not apply, and the filing of such a motion shall stay the child's removal from the United States.</p><p>The Department of Homeland Security (DHS) must provide a complete copy of a non-U.S. national's immigration file to the non-U.S. national (or the non-U.S. national's counsel) within seven days of a notice to appear for an immigration proceeding, and failure to provide the file shall result in a delay in the proceeding.</p><p>DHS must provide access to counsel for all detained non-U.S. nationals.</p><p>The Office of Refugee Resettlement must develop model guidelines for representing non-U.S. national children in immigration proceedings.</p><p>HHS must annually report on the extent to which it has provided counsel for unaccompanied children under this bill.\u00a0</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s1297"
    },
    "title": "Fair Day in Court for Kids Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fair Day in Court for Kids Act of 2025</strong></p><p>This bill provides legal protections for a <em></em>non-U.S. national (alien under federal law) who is detained or subject to immigration-related proceedings.</p><p>The Department of Justice (DOJ), or the Department of Health and Human Services (HHS) in a case involving an unaccompanied child, may appoint or provide counsel at the government's expense to non-U.S. nationals in removal proceedings and related appeals.</p><p>An unaccompanied child must be represented by counsel paid for and appointed by the government at every stage of such proceedings unless the child has obtained counsel at their own expense. If HHS fails to provide counsel to an unaccompanied child, the child's deadline for filing a motion to reopen a removal proceeding\u00a0shall not apply, and the filing of such a motion shall stay the child's removal from the United States.</p><p>The Department of Homeland Security (DHS) must provide a complete copy of a non-U.S. national's immigration file to the non-U.S. national (or the non-U.S. national's counsel) within seven days of a notice to appear for an immigration proceeding, and failure to provide the file shall result in a delay in the proceeding.</p><p>DHS must provide access to counsel for all detained non-U.S. nationals.</p><p>The Office of Refugee Resettlement must develop model guidelines for representing non-U.S. national children in immigration proceedings.</p><p>HHS must annually report on the extent to which it has provided counsel for unaccompanied children under this bill.\u00a0</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s1297"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1297is.xml"
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
      "title": "Fair Day in Court for Kids Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T03:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Day in Court for Kids Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide counsel for unaccompanied children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:27Z"
    }
  ]
}
```
