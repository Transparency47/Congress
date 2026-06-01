# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2161
- Title: Human-Animal Chimera Prohibition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2161
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-04-01T17:34:27Z
- Update date including text: 2025-04-01T17:34:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2161",
    "number": "2161",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Human-Animal Chimera Prohibition Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-01T17:34:27Z",
    "updateDateIncludingText": "2025-04-01T17:34:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:02:25Z",
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
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MD"
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
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-14",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2161ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2161\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Smith of New Jersey (for himself, Mr. Harris of Maryland , Mrs. Miller of Illinois , and Mr. Aderholt ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit certain types of human-animal chimeras.\n#### 1. Short title\nThis Act may be cited as the Human-Animal Chimera Prohibition Act of 2025 .\n#### 2. Prohibition on certain human-animal chimeras\nPart I of title 18, United States Code, is amended by inserting after chapter 51 the following:\n52 Certain Types of Human-Animal Chimeras Prohibited Sec. 1131. Definitions. 1132. Prohibition on certain human-animal chimeras. 1131. Definitions In this chapter the following definitions apply: (1) Prohibited human-animal chimera The term prohibited human-animal chimera means\u2014 (A) a human embryo into which a nonhuman cell or cells (or the component parts thereof) have been introduced to render the embryo\u2019s membership in the species Homo sapiens uncertain; (B) a human-animal embryo produced by fertilizing a human egg with nonhuman sperm; (C) a human-animal embryo produced by fertilizing a nonhuman egg with human sperm; (D) an embryo produced by introducing a nonhuman nucleus into a human egg; (E) an embryo produced by introducing a human nucleus into a nonhuman egg; (F) an embryo containing at least haploid sets of chromosomes from both a human and a nonhuman life form; (G) a nonhuman life form engineered such that human gametes develop within the body of a nonhuman life form; (H) a nonhuman life form engineered such that it contains a human brain or a brain derived wholly or predominantly from human neural tissues; (I) a nonhuman life form engineered such that it exhibits human facial features or other bodily morphologies to resemble human features; or (J) an embryo produced by mixing human and nonhuman cells, such that\u2014 (i) human gametes develop within the body of the resultant organism; (ii) it contains a human brain or a brain derived wholly or predominantly from human neural tissues; or (iii) it exhibits human facial features or other bodily morphologies to resemble human features. (2) Human embryo The term human embryo means an organism of the species Homo sapiens during the earliest stages of development, from 1 cell up to 8 weeks. 1132. Prohibition on certain human-animal chimeras (a) In general It shall be unlawful for any person to knowingly, in or otherwise affecting interstate commerce\u2014 (1) create or attempt to create a prohibited human-animal chimera; (2) transfer or attempt to transfer a human embryo into a nonhuman womb; (3) transfer or attempt to transfer a non\u00adhuman embryo into a human womb; or (4) transport or receive for any purpose a prohibited human-animal chimera. (b) Penalties (1) In general Whoever violates subsection (a) shall be fined under this title, imprisoned not more than 10 years, or both. (2) Civil penalty Whoever violates subsection (a) and derives pecuniary gain from such violation shall be subject to a civil fine of the greater of $1,000,000 and an amount equal to the amount of the gross gain multiplied by 2. (c) Rule of construction This section does not prohibit research involving the use of transgenic animal models containing human genes or transplantation of human organs, tissues, or cells into recipient animals, if such activities are not prohibited under subsection (a). .\n#### 3. Technical amendment\nThe table of chapters for part I of title 18, United States Code, is amended by inserting after the item relating to chapter 51 the following:\n52. Certain types of human-animal chimeras prohibited. .",
      "versionDate": "2025-03-14",
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
        "updateDate": "2025-04-01T17:34:27Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2161ih.xml"
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
      "title": "Human-Animal Chimera Prohibition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Human-Animal Chimera Prohibition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit certain types of human-animal chimeras.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:32Z"
    }
  ]
}
```
