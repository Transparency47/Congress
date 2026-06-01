# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4040?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4040
- Title: SALONS Stories Act
- Congress: 119
- Bill type: HR
- Bill number: 4040
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-09-23T18:27:21Z
- Update date including text: 2025-09-23T18:27:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4040",
    "number": "4040",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SALONS Stories Act",
    "type": "HR",
    "updateDate": "2025-09-23T18:27:21Z",
    "updateDateIncludingText": "2025-09-23T18:27:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:00:05Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4040ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4040\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Ms. Lee of Florida (for herself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to increase grants to combat domestic violence for States that implement domestic violence prevention training in the cosmetologist and barber licensing process, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting the Abused by Learning Options to Navigate Survivor Stories Act or the SALONS Stories Act .\n#### 2. Grant increases\nSection 2007 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10446 ) is amended by adding at the end the following:\n(l) Grant increases for States that implement domestic violence prevention training in cosmetologist and barber licensing (1) Definitions In this subsection: (A) Domestic violence prevention training The term domestic violence prevention training , with respect to training for individuals seeking licensure from a State as a cosmetologist or barber, means online or in-person training, at no cost to the individual, provided by a nonprofit anti-domestic violence organization that focuses on how to\u2014 (i) recognize the signs of domestic violence; (ii) respond to the signs of domestic violence; and (iii) refer a client of the individual to resources for victims of domestic violence. (B) Eligible State The term eligible State means a State that has in effect a law that requires each individual seeking licensure from the State as a cosmetologist or barber to undergo domestic violence prevention training. (C) State The term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, and any territory or possession of the United States. (2) Grant increase Subject to the availability of funds pursuant to paragraph (5), the Attorney General shall increase the amount of a grant awarded under subsection (a) to an eligible State by an amount that is not more than 10 percent of the average of the total amount of funding provided to the State under subsection (a) under the 3 most recent awards to the State. (3) Application An eligible State seeking a grant increase under this subsection shall submit an application to the Attorney General at such time, in such manner, and containing such information as the Attorney General may reasonably require, including information about the law of the eligible State described in paragraph (1)(B). (4) Grant increase term (A) In general The term of a grant increase under this subsection shall be for 1 year. (B) Renewal An eligible State that receives a grant increase under this subsection may submit an application for a renewal of such grant increase at such time, in such manner, and containing such information as the Attorney General may reasonably require. (C) Limit An eligible State may not receive a grant increase under this subsection for more than 3 years. (5) Authorization of appropriations There are authorized to be appropriated to carry out this subsection $5,000,000 for each of fiscal years 2026 through 2032. .",
      "versionDate": "2025-06-17",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "520",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the Abused by Learning Options to Navigate Survivor Stories Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-09T13:02:14Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4040ih.xml"
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
      "title": "SALONS Stories Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SALONS Stories Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting the Abused by Learning Options to Navigate Survivor Stories Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to increase grants to combat domestic violence for States that implement domestic violence prevention training in the cosmetologist and barber licensing process, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T12:18:22Z"
    }
  ]
}
```
