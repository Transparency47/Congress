# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/729?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/729
- Title: Teleabortion Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 729
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2026-03-26T08:06:31Z
- Update date including text: 2026-03-26T08:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/729",
    "number": "729",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001102",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Harris, Mark [R-NC-8]",
        "lastName": "Harris",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Teleabortion Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:31Z",
    "updateDateIncludingText": "2026-03-26T08:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "AL"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IL"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WY"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OH"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MO"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AZ"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "SC"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr729ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 729\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Harris of North Carolina (for himself, Mr. Clyde , Mr. Aderholt , Mr. Webster of Florida , Mr. Gill of Texas , Mrs. Miller of Illinois , Mr. Cloud , Ms. Hageman , Mr. Davidson , and Mr. Onder ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit chemical abortions performed without the presence of a healthcare provider, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Teleabortion Prevention Act of 2025 .\n#### 2. Chemical abortions prohibited without a healthcare provider present\n##### (a) Chemical abortions prohibited without a physician present\nChapter 74 of title 18, United States Code, is amended\u2014\n**(1)**\nin the chapter heading by striking Partial-Birth ; and\n**(2)**\nby inserting after section 1531 the following:\n1532. Chemical abortions prohibited without a healthcare provider physically present (a) Offense Any healthcare provider who, in or affecting interstate or foreign commerce, who knowingly provides or attempts to provide a chemical abortion\u2014 (1) without physically examining the patient; (2) without being physically present at the location of the chemical abortion; and (3) without scheduling a follow-up visit for the patient to occur not more than 14 days after the administration or use of the drug to assess the patient\u2019s physical condition, shall be fined not more than $1,000 or imprisoned not more than 2 years, or both. This subsection does not apply to a chemical abortion that is necessary to save the life of a mother whose life is endangered by a physical disorder, physical illness, or physical injury, including a life-endangering physical condition caused by or arising from the pregnancy itself. (b) No liability of the patient A patient upon whom an abortion is performed may not be prosecuted under this section or for a conspiracy to violate this section. (c) Definitions In this section: (1) Abortion drug The term abortion drug means any medicine, drug or any other substance, or any combination of drugs, medicines or substances, when it is used\u2014 (A) to intentionally kill the unborn child of a woman known to be pregnant; or (B) to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) to produce a live birth; or (ii) to remove a dead unborn child. (2) Attempts to provide In this section, the term attempts to provide , means conduct that, under the circumstances as the actor believes them to be, constitutes a substantial step in a course of conduct planned to culminate in a chemical abortion. (3) Healthcare provider The term healthcare provider means any person licensed to prescribe prescription drugs under applicable Federal and State laws. (4) Provide In this section, the term provide , means to dispense or prescribe an abortion drug, or to otherwise make an abortion drug available to a patient. (5) Chemical abortion The term chemical abortion refers to the use of an abortion drug to\u2014 (A) intentionally kill the unborn child of a woman known to be pregnant; or (B) intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) to produce a live birth; or (ii) to remove a dead unborn child. (6) Unborn child The term unborn child means an individual organism of the species homo sapiens, beginning at fertilization, until the point of being born alive as defined in section 8(b). (d) Rule of construction regarding ectopic pregnancy Nothing in this section shall be construed to have any impact on the treatment of a verified ectopic pregnancy. (e) Severability If any provision of this section or the application of such provision to any person or circumstance is held to be invalid, the remainder of this section and the application of the provisions of the remainder to any person or circumstance shall not be affected thereby. .\n##### (b) Clerical amendments\n**(1) Chapter 74**\nThe table of sections for such chapter is amended by inserting after the item relating to section 1531 the following:\n1532. Chemical abortions prohibited without a healthcare provider physically present. .\n**(2) Part I**\nThe table of chapters for part I of title 18, United States Code, is amended by striking the item relating to chapter 74, and inserting the following:\n74. Abortions 1531 .",
      "versionDate": "2025-01-24",
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
            "name": "Abortion",
            "updateDate": "2025-03-26T20:11:46Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-26T20:11:46Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-26T20:11:46Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-26T20:11:46Z"
          },
          {
            "name": "Medical ethics",
            "updateDate": "2025-03-26T20:11:46Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-03-26T20:11:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-01T13:19:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr729",
          "measure-number": "729",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-05-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr729v00",
            "update-date": "2025-05-02"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Teleabortion Prevention Act of 2025</strong></p><p>This bill restricts the use of telehealth for chemical abortions (also known as medication abortions).</p><p>Specifically, it requires a provider who dispenses or prescribes medication for a chemical abortion to physically examine the patient, be physically present at the location of the chemical abortion, and schedule a follow-up visit for the patient. The bill provides an exception for a chemical abortion that is necessary to save the life of a mother whose life is endangered by a physical disorder, illness, injury, or condition.</p><p>The bill establishes criminal penalties\u2014a fine, a prison term of up to two years, or both\u2014for a provider who does not comply with the requirements.</p><p>A patient who undergoes a chemical abortion may not be prosecuted.</p>"
        },
        "title": "Teleabortion Prevention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr729.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Teleabortion Prevention Act of 2025</strong></p><p>This bill restricts the use of telehealth for chemical abortions (also known as medication abortions).</p><p>Specifically, it requires a provider who dispenses or prescribes medication for a chemical abortion to physically examine the patient, be physically present at the location of the chemical abortion, and schedule a follow-up visit for the patient. The bill provides an exception for a chemical abortion that is necessary to save the life of a mother whose life is endangered by a physical disorder, illness, injury, or condition.</p><p>The bill establishes criminal penalties\u2014a fine, a prison term of up to two years, or both\u2014for a provider who does not comply with the requirements.</p><p>A patient who undergoes a chemical abortion may not be prosecuted.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hr729"
    },
    "title": "Teleabortion Prevention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Teleabortion Prevention Act of 2025</strong></p><p>This bill restricts the use of telehealth for chemical abortions (also known as medication abortions).</p><p>Specifically, it requires a provider who dispenses or prescribes medication for a chemical abortion to physically examine the patient, be physically present at the location of the chemical abortion, and schedule a follow-up visit for the patient. The bill provides an exception for a chemical abortion that is necessary to save the life of a mother whose life is endangered by a physical disorder, illness, injury, or condition.</p><p>The bill establishes criminal penalties\u2014a fine, a prison term of up to two years, or both\u2014for a provider who does not comply with the requirements.</p><p>A patient who undergoes a chemical abortion may not be prosecuted.</p>",
      "updateDate": "2025-05-02",
      "versionCode": "id119hr729"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr729ih.xml"
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
      "title": "Teleabortion Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Teleabortion Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit chemical abortions performed without the presence of a healthcare provider, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:42Z"
    }
  ]
}
```
