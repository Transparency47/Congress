# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8559?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8559
- Title: To amend the National Defense Authorization Act for Fiscal Year 2021 to prohibit certain institutions of higher education from receiving research and development awards, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8559
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-14T15:33:51Z
- Update date including text: 2026-05-14T15:33:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8559",
    "number": "8559",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001196",
        "district": "21",
        "firstName": "Elise",
        "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
        "lastName": "Stefanik",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "To amend the National Defense Authorization Act for Fiscal Year 2021 to prohibit certain institutions of higher education from receiving research and development awards, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-14T15:33:51Z",
    "updateDateIncludingText": "2026-05-14T15:33:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8559ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8559\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Ms. Stefanik (for herself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the National Defense Authorization Act for Fiscal Year 2021 to prohibit certain institutions of higher education from receiving research and development awards, and for other purposes.\n#### 1. Prohibition on research and development awards for certain institutions of higher education\n##### (a) In general\nSubtitle B of title II of division A of the National Defense Authorization Act for Fiscal Year 2021 is amended by inserting after section 223 ( 42 U.S.C. 6605 ) the following new section:\n223A. Prohibition on research and development awards for certain institutions of higher education (a) In general If an institution of higher education receives from a foreign source funds to carry out a specified task, such institution may not, for a period of five years after such receipt, be awarded a research and development award. (b) Definitions In this section: (1) Artificial intelligence The term artificial intelligence has the meaning given such term in section 5002. (2) Biotechnology The term biotechnology means the application of science and engineering in the direct or indirect utilization of living organisms or parts or products of such organisms, including modified forms of such organisms, parts, or products, as the case may be. (3) Foreign source The term foreign source means any of the following entities: (A) A specified foreign government. (B) An entity established under the laws of such government. (C) An entity in which such government holds ownership interest of not less than 25 percent. (D) An agent of any of the entities described in subparagraphs (A) through (C), including any of the following: (i) A subsidiary of such an entity. (ii) A person that operates primarily for the benefit of, or under the auspices of, such an entity, such as a foundation of such entity, or an educational, cultural, or language entity. (4) Institution of higher education The term institution of higher education has the meaning given such term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). (5) Quantum information science The term quantum information science has the meaning given such term in section 2 of the National Quantum Initiative Act ( 15 U.S.C. 8801 ). (6) Research and development award The term research and development award has the meaning given such term in section 223. (7) Specified foreign government The term specified foreign government means the government of any of the following countries: (A) The Bolivarian Republic of Venezuela. (B) The Democratic People\u2019s Republic of Korea. (C) The Islamic Republic of Iran. (D) The People\u2019s Republic of China. (E) The Republic of Cuba. (F) The Republic of Turkey. (G) The Russian Federation. (H) The State of Qatar. (I) Any other country the Secretary of State determines appropriate. (8) Specified task The term specified task means research and development relating to a national security or military application, including relating to any of the following: (A) Artificial intelligence. (B) Biotechnology. (C) Quantum information science. .\n##### (b) Clerical amendments\nThe National Defense Authorization Act for Fiscal Year 2021 is amended in the table of contents in section 2(b) and title II of division A by inserting after the items relating to section 223 the following new items:\nSec. 223A. Prohibition on research and development awards for certain institutions of higher education. .",
      "versionDate": "2026-04-28",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-28",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "4424",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the National Defense Authorization Act for Fiscal Year 2021 to prohibit certain institutions of higher education from receiving research and development awards, and for other purposes.",
      "type": "S"
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
        "updateDate": "2026-05-14T15:33:51Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8559ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Defense Authorization Act for Fiscal Year 2021 to prohibit certain institutions of higher education from receiving research and development awards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:32Z"
    },
    {
      "title": "To amend the National Defense Authorization Act for Fiscal Year 2021 to prohibit certain institutions of higher education from receiving research and development awards, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T08:07:23Z"
    }
  ]
}
```
