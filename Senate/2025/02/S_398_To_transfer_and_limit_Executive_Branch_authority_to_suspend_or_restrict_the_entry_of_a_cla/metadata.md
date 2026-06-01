# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/398
- Title: NO BAN Act
- Congress: 119
- Bill type: S
- Bill number: 398
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-10-17T11:03:17Z
- Update date including text: 2025-10-17T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/398",
    "number": "398",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "NO BAN Act",
    "type": "S",
    "updateDate": "2025-10-17T11:03:17Z",
    "updateDateIncludingText": "2025-10-17T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T22:46:50Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "RI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NH"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-04",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "HI"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "GA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "MD"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "DE"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s398is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 398\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Coons (for himself, Mr. Whitehouse , Mr. King , Mr. Blumenthal , Mr. Booker , Mr. Van Hollen , Mrs. Shaheen , Ms. Duckworth , Mr. Kaine , Ms. Cortez Masto , Mr. Schiff , Mr. Hickenlooper , Mrs. Murray , Mr. Wyden , Ms. Baldwin , Mr. Sanders , Mr. Durbin , Mr. Padilla , Mr. Schatz , Mr. Markey , Ms. Hirono , Mr. Warner , Mr. Welch , Mr. Luj\u00e1n , Ms. Cantwell , Mr. Peters , Ms. Warren , Ms. Klobuchar , Mr. Bennet , Ms. Smith , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo transfer and limit Executive Branch authority to suspend or restrict the entry of a class of aliens.\n#### 1. Short titles\nThis Act may be cited as the National Origin-Based Antidiscrimination for Nonimmigrants Act or the NO BAN Act .\n#### 2. Expansion of nondiscrimination provision\nSection 202(a)(1)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(1)(A) ) is amended\u2014\n**(1)**\nby striking Except as specifically provided in paragraph (2) and in sections 101(a)(27), 201(b)(2)(A)(i), and 203, no and inserting No ;\n**(2)**\nby inserting or a nonimmigrant visa, admission or other entry into the United States, or the approval or revocation of any immigration benefit after immigrant visa ;\n**(3)**\nby inserting religion, after sex, ; and\n**(4)**\nby inserting before the period at the end the following: , except as specifically provided in paragraph (2) and sections 101(a)(27), 201(b)(2)(A)(i), and 203, if otherwise expressly required by statute, or if a statutorily authorized benefit takes into consideration such factors .\n#### 3. Transfer and limitations on authority to suspend or restrict the entry of a class of aliens\nSection 212(f) of the Immigration and Nationality Act ( 8 U.S.C. 1182(f) ) is amended to read as follows:\n(f) Authority To suspend or restrict the entry of a class of aliens (1) In general Subject to paragraph (2), if the Secretary of State, in consultation with the Secretary of Homeland Security, determines, based on specific and credible facts, that the entry of any aliens or class of aliens into the United States would undermine the security or public safety of the United States or the preservation of human rights, democratic processes or institutions, or international stability, the President may temporarily\u2014 (A) suspend the entry of such aliens or class of aliens as immigrants or nonimmigrants; or (B) impose any restrictions on the entry of such aliens that the President deems appropriate. (2) Limitations In carrying out paragraph (1), the President, the Secretary of State, and the Secretary of Homeland Security shall\u2014 (A) only issue a suspension or restriction when required to address specific acts implicating a compelling government interest in a factor identified under paragraph (1); (B) narrowly tailor such suspension or restriction, using the least restrictive means, to achieve such compelling government interest; (C) specify the duration of such suspension or restriction; (D) consider waivers to any class-based restriction or suspension and apply a rebuttable presumption in favor of granting family-based and humanitarian waivers; and (E) comply with all provisions of this Act. (3) Congressional notification (A) In general Before the President may exercise the authority under paragraph (1), the Secretary of State and the Secretary of Homeland Security shall consult with Congress and provide Congress with specific evidence supporting the need for the proposed suspension or restriction and its proposed duration. (B) Briefing and report Not later than 48 hours after the President exercises the authority under paragraph (1), the Secretary of State and the Secretary of Homeland Security shall provide a briefing and submit a written report to Congress that describes\u2014 (i) the action taken pursuant to paragraph (1) and the specified objective of such action; (ii) the estimated number of individuals who will be impacted by such action; (iii) the constitutional and legislative authority under which such action took place; and (iv) the circumstances necessitating such action, including how such action complies with paragraph (2) and any intelligence informing such actions. (C) Termination If the briefing and report described in subparagraph (B) are not provided to Congress during the 48-hour period beginning when the President exercises the authority under paragraph (1), the suspension or restriction shall immediately terminate absent intervening congressional action. (D) Defined term In this paragraph, the term Congress means\u2014 (i) the Select Committee on Intelligence of the Senate ; (ii) the Committee on Foreign Relations of the Senate ; (iii) the Committee on the Judiciary of the Senate ; (iv) the Committee on Homeland Security and Governmental Affairs of the Senate ; (v) the Permanent Select Committee on Intelligence of the House of Representatives ; (vi) the Committee on Foreign Affairs of the House of Representatives ; (vii) the Committee on the Judiciary of the House of Representatives ; and (viii) the Committee on Homeland Security of the House of Representatives . (4) Publication The Secretary of State and the Secretary of Homeland Security shall publicly announce and publish an unclassified version of the report described in paragraph (3)(B) in the Federal Register. (5) Judicial review (A) In general Notwithstanding any other provision of law, an individual or entity who is present in the United States and has been harmed by a violation of this subsection may file an action in an appropriate district court of the United States to seek declaratory or injunctive relief. (B) Class action Nothing in this Act may be construed to preclude an action filed pursuant to subparagraph (A) from proceeding as a class action. (6) Treatment of commercial airlines Whenever the Secretary of Homeland Security determines that a commercial airline has failed to comply with regulations of the Secretary of Homeland Security relating to requirements of airlines for the detection of fraudulent documents used by passengers traveling to the United States (including the training of personnel in such detection), the Secretary of Homeland Security may suspend the entry of some or all aliens transported to the United States by such airline. (7) Rule of construction Nothing in this subsection may be construed as authorizing the President, the Secretary of State, or the Secretary of Homeland Security to act in a manner inconsistent with the policy decisions expressed in the immigration laws. .\n#### 4. Visa applicants report\n##### (a) Initial reports\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Homeland Security and the heads of other relevant Federal agencies, shall submit a report to the congressional committees referred to in section 212(f)(3)(D) of the Immigration and Nationality Act, as amended by section 3, that describes the implementation of Presidential Proclamations 9645, 9822, and 9983 and Executive Order Nos. 13769, 13780, and 13815, during the effective period of each such proclamation and order.\n**(2) Presidential proclamations 9645 and 9983**\nIn addition to the content described in paragraph (1), the report submitted with respect to Presidential Proclamation 9645, issued on September 24, 2017, and Presidential Proclamation 9983, issued on January 31, 2020, shall include, for each country listed in such proclamation\u2014\n**(A)**\nthe total number of individuals who applied for a visa during the period the proclamation was in effect, disaggregated by country and visa category;\n**(B)**\nthe total number of visa applicants described in subparagraph (A) who were approved, disaggregated by country and visa category;\n**(C)**\nthe total number of visa applicants described in subparagraph (A) whose applications were denied, disaggregated by country and visa category, and the reasons for such denials;\n**(D)**\nthe total number of visa applicants described in subparagraph (A) whose applications remain pending, disaggregated by country and visa category;\n**(E)**\nthe total number of visa applicants described in subparagraph (A) who were granted a waiver, disaggregated by country and visa category;\n**(F)**\nthe total number of visa applicants described in subparagraph (A) who were denied a waiver, disaggregated by country and visa category, and the reasons such waiver requests were denied;\n**(G)**\nthe total number of refugees admitted, disaggregated by country; and\n**(H)**\nthe complete reports that were submitted to the President every 180 days in accordance with section 4 of Presidential Proclamation 9645 in its original form, and as amended by Presidential Proclamation 9983.\n##### (b) Additional reports\n**(1) In general**\nNot later than 30 days after the date on which the President exercises the authority under section 212(f) of the Immigration and Nationality Act ( 8 U.S.C. 1182(f) ), as amended by section 3, and every 30 days thereafter, the Secretary of State, in coordination with the Secretary of Homeland Security and heads of other relevant Federal agencies, shall submit a report to the congressional committees referred to in paragraph (3)(D) of such section 212(f) that identifies, with respect to countries affected by a suspension or restriction\u2014\n**(A)**\nthe information described in subparagraphs (A) through (G) of subsection (a)(2); and\n**(B)**\nthe specific evidence supporting the need for the continued exercise of presidential authority under such section 212(f), including the information described in paragraph (3)(B) of such section 212(f).\n**(2) Failure to submit timely report**\nIf the Secretary of State fails to provide any report required under paragraph (1) to the appropriate congressional committees by the specified deadline, the suspension or restriction of any aliens or class of aliens pursuant to such section 212(f) shall immediately terminate absent intervening congressional action.\n**(3) Final report**\nNot later than 30 days after the termination of a suspension or restriction of any aliens or class of aliens pursuant to such section 212(f), the Secretary of State, in coordination with the Secretary of Homeland Security and the heads of other relevant Federal agencies, shall prepare and submit a final report to the congressional committees referred to in paragraph (3)(D) of such section containing the information and evidence described in subparagraphs (A) and (B) of paragraph (1).\n##### (c) Form; availability\nThe reports required under subsections (a) and (b) shall be made publicly available online in unclassified form.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the Subcommittee on Border Security and Enforcement."
      },
      "number": "924",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NO BAN Act",
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
        "name": "Immigration",
        "updateDate": "2025-03-10T17:57:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s398",
          "measure-number": "398",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-07-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s398v00",
            "update-date": "2025-07-10"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>National Origin-Based Antidiscrimination for Nonimmigrants Act or the NO BAN Act</strong></p><p>This bill imposes limitations on the President's authority to suspend or restrict aliens from entering the United States. It also prohibits religious discrimination in various immigration-related decisions, such as whether to issue an immigrant or nonimmigrant visa, unless there is a statutory basis for such discrimination.</p><p>The President may temporarily restrict the entry of any aliens or class of aliens after the Department of State determines that the restriction would address specific and credible facts that threaten U.S. interests such as public safety.</p><p>The bill also imposes limitations on such restrictions, such as requiring the President, State Department, and the Department of Homeland Security (DHS) to (1) only issue a restriction when required to address a compelling government interest, and (2) narrowly tailor the suspension to use the least restrictive means to achieve such an interest.</p><p>Before imposing a restriction, the State Department and DHS shall consult with Congress. The State Department and DHS shall report to Congress about the restriction within 48 hours of the restriction's imposition. If such a report is not made, the restriction shall immediately terminate.</p><p>Individuals or entities present in the United States and unlawfully harmed by such a restriction may sue in federal court.</p><p>The bill transfers the authority to suspend the entry of aliens traveling to the United States on a commercial airline that failed to comply with regulations related to detecting fraudulent travel documents from the Department of Justice to DHS.\u00a0</p>"
        },
        "title": "NO BAN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s398.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Origin-Based Antidiscrimination for Nonimmigrants Act or the NO BAN Act</strong></p><p>This bill imposes limitations on the President's authority to suspend or restrict aliens from entering the United States. It also prohibits religious discrimination in various immigration-related decisions, such as whether to issue an immigrant or nonimmigrant visa, unless there is a statutory basis for such discrimination.</p><p>The President may temporarily restrict the entry of any aliens or class of aliens after the Department of State determines that the restriction would address specific and credible facts that threaten U.S. interests such as public safety.</p><p>The bill also imposes limitations on such restrictions, such as requiring the President, State Department, and the Department of Homeland Security (DHS) to (1) only issue a restriction when required to address a compelling government interest, and (2) narrowly tailor the suspension to use the least restrictive means to achieve such an interest.</p><p>Before imposing a restriction, the State Department and DHS shall consult with Congress. The State Department and DHS shall report to Congress about the restriction within 48 hours of the restriction's imposition. If such a report is not made, the restriction shall immediately terminate.</p><p>Individuals or entities present in the United States and unlawfully harmed by such a restriction may sue in federal court.</p><p>The bill transfers the authority to suspend the entry of aliens traveling to the United States on a commercial airline that failed to comply with regulations related to detecting fraudulent travel documents from the Department of Justice to DHS.\u00a0</p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119s398"
    },
    "title": "NO BAN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>National Origin-Based Antidiscrimination for Nonimmigrants Act or the NO BAN Act</strong></p><p>This bill imposes limitations on the President's authority to suspend or restrict aliens from entering the United States. It also prohibits religious discrimination in various immigration-related decisions, such as whether to issue an immigrant or nonimmigrant visa, unless there is a statutory basis for such discrimination.</p><p>The President may temporarily restrict the entry of any aliens or class of aliens after the Department of State determines that the restriction would address specific and credible facts that threaten U.S. interests such as public safety.</p><p>The bill also imposes limitations on such restrictions, such as requiring the President, State Department, and the Department of Homeland Security (DHS) to (1) only issue a restriction when required to address a compelling government interest, and (2) narrowly tailor the suspension to use the least restrictive means to achieve such an interest.</p><p>Before imposing a restriction, the State Department and DHS shall consult with Congress. The State Department and DHS shall report to Congress about the restriction within 48 hours of the restriction's imposition. If such a report is not made, the restriction shall immediately terminate.</p><p>Individuals or entities present in the United States and unlawfully harmed by such a restriction may sue in federal court.</p><p>The bill transfers the authority to suspend the entry of aliens traveling to the United States on a commercial airline that failed to comply with regulations related to detecting fraudulent travel documents from the Department of Justice to DHS.\u00a0</p>",
      "updateDate": "2025-07-10",
      "versionCode": "id119s398"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s398is.xml"
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
      "title": "NO BAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NO BAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "National Origin-Based Antidiscrimination for Nonimmigrants Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to transfer and limit Executive Branch authority to suspend or restrict the entry of a class of aliens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:36Z"
    }
  ]
}
```
