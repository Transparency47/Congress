# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7983?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7983
- Title: Clean Water for All Life Act
- Congress: 119
- Bill type: HR
- Bill number: 7983
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-04-01T14:36:00Z
- Update date including text: 2026-04-01T14:36:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7983",
    "number": "7983",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Clean Water for All Life Act",
    "type": "HR",
    "updateDate": "2026-04-01T14:36:00Z",
    "updateDateIncludingText": "2026-04-01T14:36:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:01:10Z",
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
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "SC"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "CO"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "SC"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "AZ"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "VA"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7983ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7983\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mrs. Miller of Illinois (for herself, Mr. Cloud , Mr. Harrigan , Mrs. Biggs of South Carolina , Mr. Gosar , Mrs. Harshbarger , Mr. McGuire , Mr. Steube , Mr. Burchett , Ms. Boebert , Mr. Fleischmann , Mrs. Cammack , Mr. Ogles , Mr. Rose , and Mr. Norman ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit a chemical abortion without the physical presence of a healthcare provider.\n#### 1. Short title\nThis Act may be cited as the Clean Water for All Life Act .\n#### 2. Chemical abortions prohibited without a health care provider physically present\n##### (a) In general\nChapter 74 of title 18, United States Code, is amended\u2014\n**(1)**\nin the header by striking Partial-Birth Abortions and inserting Abortion Crimes ; and\n**(2)**\nby inserting at the end the following:\n1532. Chemical abortions prohibited without a health care provider physically present (a) Offense Whoever, in or affecting interstate commerce, provides or attempts to provide abortion through a chemical abortion drug\u2014 (1) without physically examining the patient; (2) without being physically present at the location of the chemical abortion; and (3) without providing a catch kit and red bag medical waste, including instructions for the patient to bring such kit and bag to the healthcare provider for proper disposal; shall be imprisoned not more than 5 years, fined not more than $50,000, or both, per occurrence. (b) Definitions In this section: (1) Abortion The term abortion \u2014 (A) means the act of using, prescribing, administering, procuring, or selling of any instrument, medicine, drug, or any other substance, device, or means with the purpose to terminate the pregnancy of a woman, with knowledge that the termination by any of those means will with reasonable likelihood cause the death of the unborn child; and (B) does not mean an act described under subparagraph (A) if the act is performed with the purpose to\u2014 (i) save the life or preserve the health of the unborn child; (ii) remove a dead unborn child caused by spontaneous abortion; or (iii) remove an ectopic pregnancy. (2) Catch kit The term catch kit means a collection container designed to catch and hold medical waste or infectious waste, often used for collecting samples for testing. (3) Chemical abortion drug The term chemical abortion drug means\u2014 (A) mifepristone, misoprostol, mifeprex, mifegyne, or any substantially similar generic or non-generic drug or chemical dispensed for purposes of causing an abortion; or (B) any drug developed, marketed, sold, or distributed for the purpose of causing an abortion. (4) Fertilization The term fertilization means the fusion of a human spermatozoon with a human ovum. (5) Red bag medical waste The term red bag medical waste means a biohazardous waste container made to contain medical or biohazardous waste. The container must either\u2014 (A) be red with lettering and symbols in a contrasting color; or (B) include such required warning labels in fluorescent orange or orange-red, with lettering and symbols in a contrasting color. (6) Unborn child The term unborn child means an individual organism of the species homo sapiens from fertilization until live birth. .\n##### (b) Clerical amendment\nThe table of sections for chapter 74 of title 18, United States Code, is amended by adding at the end the following:\n1532. Chemical abortions prohibited without a health care provider physically present. .",
      "versionDate": "2026-03-18",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-01T14:36:00Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7983ih.xml"
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
      "title": "Clean Water for All Life Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Water for All Life Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit a chemical abortion without the physical presence of a healthcare provider.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T04:48:25Z"
    }
  ]
}
```
