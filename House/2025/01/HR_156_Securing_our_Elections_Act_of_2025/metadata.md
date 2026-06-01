# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/156
- Title: Securing our Elections Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 156
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-24T20:35:41Z
- Update date including text: 2025-02-24T20:35:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/156",
    "number": "156",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Securing our Elections Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-24T20:35:41Z",
    "updateDateIncludingText": "2025-02-24T20:35:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-03T16:15:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr156ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 156\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo ensure election integrity and security by establishing consistent photo identification requirements for voting in elections for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing our Elections Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nFree, fair, and secure elections are necessary to the prosperity of democracy in the United States and around the world.\n**(2)**\nThe right to vote is a crucial aspect of American citizenship and must be protected from any potential interference, abuse, and fraud.\n**(3)**\nThe passage of the Help America Vote Act of 2002 improved and standardized State and local governments\u2019 administration of Federal elections, but lacked strong provisions to validate a voter\u2019s identity prior to their voting.\n**(4)**\nIn 2005, the bipartisan Commission on Federal Election Reform co-chaired by former Democratic President Jimmy Carter and former Republican Secretary of State James A. Baker III released a report which explicitly recommended that States require voters to use a valid identification that includes their full legal name, date of birth, a signature, and a photo.\n**(5)**\nA public survey conducted by the reputable, nonpartisan Monmouth University Polling Institute in June 2021 indicated that an overwhelming 80 percent of Americans support requiring voters to show a photo identification in order to vote.\n**(6)**\nValid identification is required by the States and the Federal Government for a multitude of serious purposes in public life such as driving or renting a car, boarding an airplane or train, traveling within and outside of the United States, purchasing alcohol or controlled substances, picking up prescription medication, opening a bank account or cashing a check, applying for employment or housing opportunities, and much more.\n**(7)**\nAs determined by the Congressional Research Service, 161 nations worldwide\u2014approximately 83 percent\u2014require their citizens to present a form of identification in order to vote, including 38 of the top 50 most democratic nations identified by the Democracy Index 2021.\n**(8)**\nMore than two-thirds of the States already request or require citizens to show a form of identification in order to vote, 22 of which request or require a photo identification for the purposes of voting.\n#### 3. Requiring voters to provide photo identification\n##### (a) Requirement To provide photo identification as condition of casting ballot\n**(1) In general**\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended by inserting after section 303 the following new section:\n303A. Photo identification requirements (a) Provision of identification required as condition of casting ballot (1) Individuals voting in person (A) Requirement to provide identification Notwithstanding any other provision of law and except as provided in subparagraph (B), the appropriate State or local election official may not provide a ballot for an election for Federal office to an individual who desires to vote in person unless the individual presents to the official a valid photo identification. (B) Availability of provisional ballot (i) In general If an individual does not present the identification required under subparagraph (A), the individual shall be permitted to cast a provisional ballot with respect to the election under section 302(a), except that the appropriate State or local election official may not make a determination under section 302(a)(4) that the individual is eligible under State law to vote in the election unless, not later than 3 days after casting the provisional ballot, the individual presents to the official\u2014 (I) the identification required under subparagraph (A); or (II) an affidavit developed and made available to the individual by the State attesting that the individual does not possess the identification required under subparagraph (A) because the individual has a religious objection to being photographed. (ii) No effect on other provisional balloting rules Nothing in clause (i) may be construed to apply to the casting of a provisional ballot pursuant to section 302(a) or any State law for reasons other than the failure to present the identification required under subparagraph (A). (2) Individuals voting other than in person (A) In general Notwithstanding any other provision of law and except as provided in subparagraph (B), the appropriate State or local election official may not accept any ballot for an election for Federal office provided by an individual who votes other than in person unless the individual submits with the ballot\u2014 (i) a copy of a valid photo identification; or (ii) the last four digits of the individual\u2019s Social Security number and an affidavit developed and made available to the individual by the State attesting that the individual is unable to obtain a copy of a valid photo identification after making reasonable efforts to obtain such a copy. (B) Exception for overseas military voters Subparagraph (A) does not apply with respect to a ballot provided by an absent uniformed services voter who, by reason of active duty or service, is absent from the United States on the date of the election involved. In this subparagraph, the term absent uniformed services voter has the meaning given such term in section 107(1) of the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20310(1) ), other than an individual described in section 107(1)(C) of such Act. (b) Providing certain assistance to individuals unable To pay costs of obtaining identification or otherwise unable To obtain identification (1) Provision of identification without charge to certain individuals If an individual presents a State official at the appropriate State agency or department designated by the State with an affidavit developed and made available to the individual by the State attesting that the individual is unable to pay the costs associated with obtaining a valid photo identification under this section, or attesting that the individual is otherwise unable to obtain a valid photo identification under this section after making reasonable efforts to obtain such an identification, the official shall provide the individual with a valid photo identification under this subsection without charge to the individual. (2) Public access to digital imaging devices With respect to each State, the appropriate State or local government official of the State shall ensure, to the extent practicable, public access to a digital imaging device, which shall include a printer, copier, image scanner, or multifunction machine, at State and local government buildings in the State, including courts, libraries, and police stations, for the purpose of allowing individuals to use such a device at no cost to the individual to make a copy of a valid photo identification. (c) Valid photo identifications described For purposes of this section, a valid photo identification means, with respect to an individual who seeks to vote in a State, any of the following: (1) A valid State-issued motor vehicle driver\u2019s license that includes a photo of the individual and an expiration date. (2) A valid State-issued identification card that includes a photo of the individual and an expiration date. (3) A valid United States passport for the individual. (4) A valid military identification for the individual. (5) Any other form of government-issued identification that the State may specify as a valid photo identification for purposes of this subsection. (d) Notification of identification requirement to applicants for voter registration (1) In general Each State shall ensure that, at the time an individual applies to register to vote in elections for Federal office in the State, the appropriate State or local election official notifies the individual of the photo identification requirements of this section. (2) Special rule for individuals applying to register to vote online Each State shall ensure that, in the case of an individual who applies to register to vote in elections for Federal office in the State online, the online voter registration system notifies the individual of the photo identification requirements of this section before the individual completes the online registration process. (e) Treatment of States with certain photo identification requirements in effect as of date of enactment If, as of the date of the enactment of this section, a State has in effect a law that satisfies or exceeds the requirements of this section for an individual to provide a photo identification as a condition of casting a ballot in elections for Federal office held in the State and the law remains in effect on and after the effective date of this section, the State shall be considered to meet the requirements of this section if\u2014 (1) the State submits a request to the Attorney General and provides such information as the Attorney General may consider necessary to determine that the State has in effect such a law and that the law remains in effect; and (2) the Attorney General\u2014 (A) approves the request; or (B) fails to issue a determination with respect to the request during the 180-day period that begins on the date the State submits such request. (f) Effective date This section shall apply with respect to elections for Federal office held in 2026 or any succeeding year. .\n**(2) Clerical amendment**\nThe table of contents of such Act is amended by inserting after the item relating to section 303 the following new item:\nSec. 303A. Photo identification requirements. .\n##### (b) Conforming amendment relating to voluntary guidance by Election Assistance Commission\nSection 311(b) of such Act ( 52 U.S.C. 21101(b) ) is amended\u2014\n**(1)**\nby striking and at the end of paragraph (2);\n**(2)**\nby striking the period at the end of paragraph (3) and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(4) in the case of the recommendations with respect to section 303A, October 1, 2025. .\n##### (c) Conforming amendment relating to enforcement\nSection 401 of such Act ( 52 U.S.C. 21111 ) is amended by striking 303, and 304 and inserting 303, 303A, and 304 .\n##### (d) Conforming amendments relating to repeal of existing photo identification requirements for certain voters\n**(1) In general**\nSection 303 of such Act ( 52 U.S.C. 21083 ) is amended\u2014\n**(A)**\nin the heading, by striking and requirements for voters who register by mail ;\n**(B)**\nin the heading of subsection (b), by striking for Voters Who Register by Mail and inserting for Mail-In Registration Forms ;\n**(C)**\nin subsection (b), by striking paragraphs (1) through (3) and redesignating paragraphs (4) and (5) as paragraphs (1) and (2), respectively; and\n**(D)**\nin subsection (c), by striking subsections (a)(5)(A)(i)(II) and (b)(3)(B)(i)(II) and inserting subsection (a)(5)(A)(i)(II) .\n**(2) Clerical Amendment**\nThe table of contents of such Act is amended by amending the item relating to section 303 to read as follows:\nSec. 303. Computerized statewide voter registration list requirements. .\n##### (e) Effective Date\nThis section and the amendments made by this section shall apply with respect to elections for Federal office held in 2026 or any succeeding year.",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2025-02-19T21:00:53Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-02-19T21:00:53Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-19T21:00:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T14:06:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
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
          "measure-id": "id119hr156",
          "measure-number": "156",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr156v00",
            "update-date": "2025-02-24"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing our Elections Act of 2025</strong></p><p>This bill establishes certain photo identification requirements for voting in federal elections.</p><p>Specifically, the bill prohibits a state or local election official from providing a ballot for a federal election to an individual who does not present valid photo identification.</p><p>Next, the bill outlines the availability of provisional ballots and the requirements for counting those ballots. In particular, an individual who does not present a valid photo identification must be permitted to cast a provisional ballot. However, an election official may not determine that the individual is eligible under state law to vote in the election unless, not later than three days after casting the provisional ballot, the individual presents (1) the identification required, or (2) an affidavit attesting that the individual does not possess the identification because of a religious objection to being photographed.</p><p>An election official may not allow for voting methods other than in-person voting unless the individual submits the ballot with (1) a copy of their photo identification, or (2) the last four digits of their Social Security number with an affidavit attesting that the individual is unable to obtain a copy of a valid photo identification after making reasonable efforts to obtain a copy. This prohibition shall not apply to overseas military voters.</p><p>The bill also requires a state to provide an individual with a valid photo identification without charge if that individual presents an affidavit attesting to an inability to afford or otherwise obtain a valid photo identification.</p>"
        },
        "title": "Securing our Elections Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr156.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing our Elections Act of 2025</strong></p><p>This bill establishes certain photo identification requirements for voting in federal elections.</p><p>Specifically, the bill prohibits a state or local election official from providing a ballot for a federal election to an individual who does not present valid photo identification.</p><p>Next, the bill outlines the availability of provisional ballots and the requirements for counting those ballots. In particular, an individual who does not present a valid photo identification must be permitted to cast a provisional ballot. However, an election official may not determine that the individual is eligible under state law to vote in the election unless, not later than three days after casting the provisional ballot, the individual presents (1) the identification required, or (2) an affidavit attesting that the individual does not possess the identification because of a religious objection to being photographed.</p><p>An election official may not allow for voting methods other than in-person voting unless the individual submits the ballot with (1) a copy of their photo identification, or (2) the last four digits of their Social Security number with an affidavit attesting that the individual is unable to obtain a copy of a valid photo identification after making reasonable efforts to obtain a copy. This prohibition shall not apply to overseas military voters.</p><p>The bill also requires a state to provide an individual with a valid photo identification without charge if that individual presents an affidavit attesting to an inability to afford or otherwise obtain a valid photo identification.</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr156"
    },
    "title": "Securing our Elections Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing our Elections Act of 2025</strong></p><p>This bill establishes certain photo identification requirements for voting in federal elections.</p><p>Specifically, the bill prohibits a state or local election official from providing a ballot for a federal election to an individual who does not present valid photo identification.</p><p>Next, the bill outlines the availability of provisional ballots and the requirements for counting those ballots. In particular, an individual who does not present a valid photo identification must be permitted to cast a provisional ballot. However, an election official may not determine that the individual is eligible under state law to vote in the election unless, not later than three days after casting the provisional ballot, the individual presents (1) the identification required, or (2) an affidavit attesting that the individual does not possess the identification because of a religious objection to being photographed.</p><p>An election official may not allow for voting methods other than in-person voting unless the individual submits the ballot with (1) a copy of their photo identification, or (2) the last four digits of their Social Security number with an affidavit attesting that the individual is unable to obtain a copy of a valid photo identification after making reasonable efforts to obtain a copy. This prohibition shall not apply to overseas military voters.</p><p>The bill also requires a state to provide an individual with a valid photo identification without charge if that individual presents an affidavit attesting to an inability to afford or otherwise obtain a valid photo identification.</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr156"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr156ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Securing our Elections Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing our Elections Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T23:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure election integrity and security by establishing consistent photo identification requirements for voting in elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T23:33:16Z"
    }
  ]
}
```
