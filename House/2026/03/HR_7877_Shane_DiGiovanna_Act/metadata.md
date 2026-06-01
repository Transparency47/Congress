# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7877?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7877
- Title: Shane DiGiovanna Act
- Congress: 119
- Bill type: HR
- Bill number: 7877
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-03T08:05:48Z
- Update date including text: 2026-04-03T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-17 - IntroReferral: Sponsor introductory remarks on measure. (CR H2535)
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-17 - IntroReferral: Sponsor introductory remarks on measure. (CR H2535)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7877",
    "number": "7877",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000601",
        "district": "1",
        "firstName": "Greg",
        "fullName": "Rep. Landsman, Greg [D-OH-1]",
        "lastName": "Landsman",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Shane DiGiovanna Act",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:48Z",
    "updateDateIncludingText": "2026-04-03T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2535)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "NJ"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7877ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7877\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Landsman introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Health and Human Services to establish a demonstration program to test mandatory coverage of treatment for wound care for epidermolysis bullosa under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Shane DiGiovanna Act .\n#### 2. Demonstration program to test mandatory coverage of treatment for wound care for epidermolysis bullosa under the Medicaid program\n##### (a) In general\nBeginning not later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services (in this section referred to as the Secretary ) shall conduct a 2-year demonstration program under which items and services specified in subsection (b) furnished for the treatment of epidermolysis bullosa are required to be included as medical assistance under a State plan (or waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) for individuals described in section 1902(a)(10)(A)(i) of such Act ( 42 U.S.C. 1396a(a)(10)(A)(i) ).\n##### (b) Specified items and services\nFor purposes of subsection (a), the items and services specified in this subsection are over-the-counter antihistamines, acetaminophen, nonsteroidal anti-inflammatory drugs, antiseptics, zinc oxide, antibiotic ointments, and necessary wound care supplies, including wound care dressings (inclusive of primary and secondary dressings), gauze, and bandage retainers.\n##### (c) Scope of demonstration\nThe Secretary shall conduct the demonstration program described in subsection (a) on a nationwide basis.\n##### (d) Study\nNot later than 1 year after the end of the demonstration program described in subsection (a), the Secretary shall submit to Congress a report on such program. Such report shall include the following:\n**(1)**\nAn evaluation of the effect of such program on expenditures for treatment of individuals with epidermolysis bullosa under the Medicaid program (taking into account any such treatment avoided due to such program).\n**(2)**\nAn analysis of health outcomes for such individuals compared to such outcomes before such program.\n**(3)**\nAny recommendations relating to how to prevent hospitalizations relating to epidermolysis bullosa.",
      "versionDate": "2026-03-09",
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
        "name": "Health",
        "updateDate": "2026-04-02T18:33:50Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7877ih.xml"
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
      "title": "Shane DiGiovanna Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shane DiGiovanna Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to establish a demonstration program to test mandatory coverage of treatment for wound care for epidermolysis bullosa under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:36Z"
    }
  ]
}
```
