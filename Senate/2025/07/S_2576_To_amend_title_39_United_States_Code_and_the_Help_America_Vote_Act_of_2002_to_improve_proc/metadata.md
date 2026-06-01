# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2576?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2576
- Title: Election Mail Act
- Congress: 119
- Bill type: S
- Bill number: 2576
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-04-07T11:52:38Z
- Update date including text: 2026-04-07T11:52:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2576",
    "number": "2576",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Election Mail Act",
    "type": "S",
    "updateDate": "2026-04-07T11:52:38Z",
    "updateDateIncludingText": "2026-04-07T11:52:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T16:19:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2576is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2576\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Ms. Klobuchar introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend title 39, United States Code, and the Help America Vote Act of 2002 to improve procedures and requirements related to election mail.\n#### 1. Short title\nThis Act may be cited as the Election Mail Act .\n#### 2. Same-day processing of absentee ballots\n##### (a) In general\nChapter 34 of title 39, United States Code, is amended by adding at the end the following:\n3407. Same-day processing of ballots (a) In general The Postal Service shall ensure, to the maximum extent practicable, that any ballot carried by the Postal Service is processed by and cleared from any postal facility or post office on the same day that the ballot is received by that postal facility or post office. (b) Definitions As used in this section\u2014 (1) the term ballot means any ballot transmitted by a voter by mail in an election for Federal office, but does not include any ballot covered by section 3406; and (2) the term election for Federal office means a general, special, primary, or runoff election for the office of President or Vice President, or of Senator or Representative in, or Delegate or Resident Commissioner to, the Congress. .\n##### (b) Technical and conforming amendments\n**(1) Chapter heading**\nThe heading for chapter 34 of title 39, United States Code, is amended by striking Armed Forces and Free Postage and inserting Armed Forces; Free Postage; Election Mail .\n**(2) Table of chapters**\nThe table of chapters for part IV of title 39, United States Code, is amended by striking the item relating to chapter 34 and inserting the following:\n34. Armed Forces; Free Postage; Election Mail 3401 .\n**(3) Table of sections**\nThe table of sections for chapter 34 of title 39, United States Code, is amended by adding at the end the following:\n3407. Same-day processing of ballots. .\n##### (c) Effective date\nThe amendments made by this subsection shall apply to absentee ballots relating to an election for Federal office occurring on or after the date that is 60 days after the date of enactment of this Act.\n#### 3. Intelligent mail barcodes for ballots\n##### (a) In general\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 ) is amended\u2014\n**(1)**\nby redesignating section 311 and section 312 as sections 321 and 322, respectively;\n**(2)**\nby redesignating subtitle B as subtitle C; and\n**(3)**\nby inserting after subtitle A the following new subtitle:\nB Requirements relating to mailed ballots 311. Use of intelligent mail barcodes (a) In general Each State and jurisdiction shall provide with each ballot for an election for Federal office that is sent by mail a return envelope that contains an intelligent mail barcode, as prescribed by the United States Postal Service. (b) Exception Subsection (a) shall not apply to any ballot for which a State or jurisdiction uses an alternative system that enables voters to track the ballot through the mail. (c) State For purposes of this section, the term State includes the District of Columbia, the Commonwealth of Puerto Rico, Guam, American Samoa, the United States Virgin Islands, and the Commonwealth of the Northern Mariana Islands. (d) Effective date The requirements of this section shall apply to elections for Federal office occurring on or after January 1, 2026. .\n##### (b) Enforcement\nSection 401 of the Help America Vote Act of 2002 ( 52 U.S.C. 21111 ) is amended by inserting or the requirements relating to mailed ballots under subtitle B of title III before the period at the end.\n##### (c) Conforming amendment\nSection 321(a) of such Act ( 52 U.S.C. 21101 ), as redesignated by subsection (a), is amended by striking section 312 and inserting section 322 .\n##### (d) Clerical amendments\nThe table of contents of such Act is amended\u2014\n**(1)**\nby striking Subtitle B\u2014Voluntary and inserting Subtitle C\u2014Voluntary ;\n**(2)**\nby redesignating the items relating to sections 311 and 312 as relating to sections 321 and 322, respectively; and\n**(3)**\nby inserting after the item relating to section 305 the following:\nSubtitle B\u2014Requirements relating to mailed ballots Sec. 311. Use of intelligent mail barcodes. .\n#### 4. Election mail and delivery improvements\n##### (a) Postmark required for ballots\n**(1) In general**\nChapter 34 of title 39, United States Code, as amended by section 2, is amended by adding at the end the following:\n3408. Postmark required for ballots (a) In general In the case of any absentee ballot carried by the Postal Service, the Postal Service shall indicate on the ballot envelope, using a postmark or otherwise\u2014 (1) the fact that the ballot was carried by the Postal Service; and (2) the date on which the ballot was mailed. (b) Definitions As used in this section\u2014 (1) the term absentee ballot means any ballot transmitted by a voter by mail in an election for Federal office, but does not include any ballot covered by section 3406; and (2) the term election for Federal office means a general, special, primary, or runoff election for the office of President or Vice President, or of Senator or Representative in, or Delegate or Resident Commissioner to, the Congress. .\n**(2) Technical and conforming amendment**\nThe table of sections for chapter 34 of title 39, United States Code, as amended by section 2, is amended by adding at the end the following:\n3408. Postmark required for ballots. .\n**(3) Effective date**\nThe amendments made by this subsection shall apply to absentee ballots relating to an election for Federal office occurring on or after the date that is 60 days after the date of enactment of this Act.\n##### (b) Greater visibility for ballots\n**(1) In general**\nSubtitle C of title III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ), as added by section 3, is amended by adding at the end the following new section:\n312. Ballot visibility (a) In general Each State or local election official shall\u2014 (1) affix Tag 191, Domestic and International Mail-In Ballots (or any successor tag designated by the United States Postal Service), to any tray or sack of official ballots relating to an election for Federal office that is destined for a domestic or international address; (2) use the Official Election Mail logo to designate official ballots relating to an election for Federal office that is destined for a domestic or international address; and (3) if an intelligent mail barcode (as described in section 311) is utilized for any official ballot relating to an election for Federal office that is destined for a domestic or international address, ensure the specific ballot service type identifier for such mail is visible. (b) Effective date The requirements of this section shall apply to elections for Federal office occurring on and after the date that is 60 days after the date of enactment of this section. .\n**(2) Issuance of voluntary guidance by election assistance commission**\nSection 321(b) of such Act ( 52 U.S.C. 21101(b) ), as redesignated by section 3, is amended\u2014\n**(A)**\nby striking and at the end of paragraph (2);\n**(B)**\nby striking the period at the end of paragraph (3) and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(4) in the case of the recommendations with respect to section 312, the date described in section 312(b). .\n**(3) Clerical amendment**\nThe table of contents of such Act, as amended by section 3, is amended by inserting after the item relating to section 311 the following new item:\nSec. 312. Ballot visibility. .\n#### 5. Carriage of election mail\n##### (a) Treatment of election mail\n**(1) Treatment as first-class mail; free postage**\nChapter 34 of title 39, United States Code, as amended by section 4(a), is amended by adding at the end the following:\n3409. Domestic election mail; restriction of operational changes prior to elections (a) Definitions In this section: (1) Election for Federal office The term election for Federal office means a general, special, primary, or runoff election for the office of President or Vice President, or of Senator or Representative in, or Delegate or Resident Commissioner to, the Congress. (2) Election mail The term election mail means\u2014 (A) a blank or completed voter registration application form, voter registration card, or similar materials, relating to an election for Federal office; (B) a blank or completed absentee and other mail-in ballot application form, and a blank or completed absentee or other mail-in ballot, relating to an election for Federal office, and (C) other materials relating to an election for Federal office that are mailed by a State or local election official to an individual who is registered to vote. (b) Carriage of election mail Election mail (other than balloting materials covered under section 3406 (relating to the Uniformed and Overseas Absentee Voting Act)), individually or in bulk, shall be carried in accordance with the service standards established for first-class mail under section 3691. (c) No postage required for completed ballots Completed absentee or other mail-in ballots (other than balloting materials covered under section 3406 (relating to the Uniformed and Overseas Absentee Voting Act)) shall be carried free of postage. (d) Restriction of operational changes During the 120-day period that ends on the date of an election for Federal office, the Postal Service may not carry out any operational change that would restrict the prompt and reliable delivery of election mail. This subsection applies to operational changes which include\u2014 (1) removing or eliminating any mail collection box without immediately replacing it; and (2) removing, decommissioning, or any other form of stopping the operation of mail sorting machines, other than for routine maintenance. (e) Election mail coordinator The Postal Service shall appoint an Election Mail Coordinator at each area office and district office to facilitate relevant information sharing with State, territorial, local, and Tribal election officials in regards to the mailing of election mail. .\n**(2) Reimbursement of Postal Service for revenue forgone**\nSection 2401(c) of title 39, United States Code, is amended by striking sections 3217 and 3403 through 3406 and inserting sections 3217, 3403 through 3406, and 3409 .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 34 of title 39, United States Code, as amended by section 4(a), is amended by adding at the end the following:\n3409. Domestic election mail; restriction of operational changes prior to elections. .\n##### (c) Effective date\nThe amendments made by this section shall take effect upon the expiration of the 180-day period that begins on the date of enactment of this section.\n#### 6. United States Postal Service consultation\n##### (a) In general\nThe Postmaster General shall consult with Indian Tribes, on an annual basis, regarding issues relating to the United States Postal Service that present barriers to voting for eligible voters living on Indian lands.\n##### (b) Definitions\nFor purposes of this section\u2014\n**(1) Indian lands**\nThe term Indian lands means\u2014\n**(A)**\nany Indian country, as such term is defined in section 1151 of title 18, United States Code, of an Indian Tribe;\n**(B)**\nany land in Alaska that is owned, pursuant to the Alaska Native Claims Settlement Act ( 43 U.S.C. 1601 et seq. ), by\u2014\n**(i)**\nan Indian Tribe that is a Native village (as such term is defined in section 3 of such Act ( 43 U.S.C. 1602 )); or\n**(ii)**\na Village Corporation (as such term is defined in such section 3) that is associated with an Indian Tribe described in clause (i);\n**(C)**\nany land on which the seat of government of an Indian Tribe is located; and\n**(D)**\nany land that is part or all of a Tribal designated statistical area associated with an Indian Tribe, or is part or all of an Alaska Native village statistical area associated with an Indian Tribe, as defined by the Bureau of the Census for the purposes of the most recent decennial census.\n**(2) Indian Tribe**\nThe term Indian Tribe means the recognized governing body of any Indian or Alaska Native Tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ).\n#### 7. Uniform deadline for acceptance of mailed ballots\n##### (a) In general\nSubtitle C of title III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ), as added by section 3 and amended by section 4, is amended by adding at the end the following new section:\n313. Uniform deadline for acceptance of mailed ballots (a) In general A State or local election official may not refuse to accept or process a ballot submitted by an individual by mail with respect to an election for Federal office in the State on the grounds that the individual did not meet a deadline for returning the ballot to the appropriate State or local election official if\u2014 (1) the ballot is postmarked or otherwise indicated by the United States Postal Service to have been mailed on or before the date of the election; and (2) the ballot is received by the appropriate election official prior to the expiration of the 7-day period which begins on the date of the election. (b) Rule of construction Nothing in this section shall be construed to prohibit a State from having a law that allows for counting of ballots in an election for Federal office that are received through the mail after the date that is 7 days after the date of the election. (c) Effective date This section shall apply with respect to the regularly scheduled general election for Federal office held in November 2026 and each succeeding election for Federal office. .\n##### (b) Clerical amendment\nThe table of contents of such Act, as amended by sections 3 and 4, is amended by inserting after the item relating to section 312 the following new item:\nSec. 313. Uniform deadline for acceptance of mailed ballots. .",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-08-05",
        "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4915",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Election Mail Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-15T18:04:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
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
          "measure-id": "id119s2576",
          "measure-number": "2576",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2576v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Election Mail Act</strong></p><p>This bill addresses the delivery and processing of election mail for federal elections, including by establishing certain standards for mail-in ballots.</p><p>Specifically, the bill requires the U.S. Postal Service (USPS) to</p><ul><li>ensure (to the maximum extent practicable) same-day processing of mail-in ballots,</li><li>postmark each ballot,</li><li>carry election mail (e.g., voter registration applications and mail-in ballots) as first-class mail that is free of postage,</li><li>appoint an election mail coordinator at each area office and district office, and</li><li>consult annually with Indian tribes regarding barriers to voting for eligible voters living on Indian lands.</li></ul><p>The bill prohibits the USPS, within 120 days of a federal election, from making any operational change that would restrict the prompt and reliable delivery of election mail.</p><p>Each state and jurisdiction must provide with each mail-in ballot a return envelope with an intelligent mail barcode. This requirement does not apply to a state or jurisdiction that uses an alternative system that enables voters to track the ballot through the mail.</p><p>The bill requires election officials to count mail-in ballots that are postmarked by election day and arrive within seven days after the election.</p>"
        },
        "title": "Election Mail Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2576.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Election Mail Act</strong></p><p>This bill addresses the delivery and processing of election mail for federal elections, including by establishing certain standards for mail-in ballots.</p><p>Specifically, the bill requires the U.S. Postal Service (USPS) to</p><ul><li>ensure (to the maximum extent practicable) same-day processing of mail-in ballots,</li><li>postmark each ballot,</li><li>carry election mail (e.g., voter registration applications and mail-in ballots) as first-class mail that is free of postage,</li><li>appoint an election mail coordinator at each area office and district office, and</li><li>consult annually with Indian tribes regarding barriers to voting for eligible voters living on Indian lands.</li></ul><p>The bill prohibits the USPS, within 120 days of a federal election, from making any operational change that would restrict the prompt and reliable delivery of election mail.</p><p>Each state and jurisdiction must provide with each mail-in ballot a return envelope with an intelligent mail barcode. This requirement does not apply to a state or jurisdiction that uses an alternative system that enables voters to track the ballot through the mail.</p><p>The bill requires election officials to count mail-in ballots that are postmarked by election day and arrive within seven days after the election.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2576"
    },
    "title": "Election Mail Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Election Mail Act</strong></p><p>This bill addresses the delivery and processing of election mail for federal elections, including by establishing certain standards for mail-in ballots.</p><p>Specifically, the bill requires the U.S. Postal Service (USPS) to</p><ul><li>ensure (to the maximum extent practicable) same-day processing of mail-in ballots,</li><li>postmark each ballot,</li><li>carry election mail (e.g., voter registration applications and mail-in ballots) as first-class mail that is free of postage,</li><li>appoint an election mail coordinator at each area office and district office, and</li><li>consult annually with Indian tribes regarding barriers to voting for eligible voters living on Indian lands.</li></ul><p>The bill prohibits the USPS, within 120 days of a federal election, from making any operational change that would restrict the prompt and reliable delivery of election mail.</p><p>Each state and jurisdiction must provide with each mail-in ballot a return envelope with an intelligent mail barcode. This requirement does not apply to a state or jurisdiction that uses an alternative system that enables voters to track the ballot through the mail.</p><p>The bill requires election officials to count mail-in ballots that are postmarked by election day and arrive within seven days after the election.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2576"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2576is.xml"
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
      "title": "Election Mail Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Election Mail Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 39, United States Code, and the Help America Vote Act of 2002 to improve procedures and requirements related to election mail.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:29Z"
    }
  ]
}
```
