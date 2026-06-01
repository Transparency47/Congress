# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1056?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1056
- Title: Home-Based Telemental Health Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1056
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-01-15T13:22:59Z
- Update date including text: 2026-01-15T13:22:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1056",
    "number": "1056",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Home-Based Telemental Health Care Act of 2025",
    "type": "S",
    "updateDate": "2026-01-15T13:22:59Z",
    "updateDateIncludingText": "2026-01-15T13:22:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T20:58:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "MN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "AR"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1056is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1056\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Rounds (for himself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a home-based telemental health care grant program for purposes of increasing mental health and substance use services in rural medically underserved populations and for individuals in farming, fishing, and forestry occupations.\n#### 1. Short title\nThis Act may be cited as the Home-Based Telemental Health Care Act of 2025 .\n#### 2. Mental health and substance use services delivered to rural underserved populations via telemental health care\nTitle III of the Public Health Service Act is amended by inserting after section 330K ( 42 U.S.C. 254c\u201316 ) the following:\n330K\u20131. Mental health and substance use services delivered to rural underserved populations via telemental health care (a) Definitions In this section\u2014 (1) the term covered populations means\u2014 (A) health professional shortage areas (as defined in section 332(a)(1)) in rural areas; or (B) populations engaged in a farming, fishing, or forestry industry; (2) the term eligible entity means a public or nonprofit private telemental health provider network that offers services that include mental health and substance use services provided by professionals trained in mental health and substance use; (3) the term farming, fishing, or forestry industry means an occupation defined as a farming, fishing, or forestry occupation by the Department of Labor in accordance with the Standard Occupational Classification System; (4) the term home-based telemental means the use of telemental health services where the patient is in his or her own home or other place of comfort; (5) the term professional trained in mental health means a psychiatrist, a qualified mental health professional (as defined in section 330K), or another mental health professional acting under the direction of a psychiatrist; (6) the term rural has the meaning given such term by the Office of Rural Health Policy of the Health Resources and Services Administration; and (7) the term telemental health means the use of electronic information and telecommunications technologies to support long distance clinical health care, patient and professional health-related education, public health, and health administration. (b) Program authorized The Secretary, in consultation with the Rural Health Liaison of the Department of Agriculture, shall award grants to eligible entities to expand and enhance access to mental health and substance use services for covered populations in their homes or other places of comfort, as delivered remotely by professionals trained in mental health and substance use using telemental health care. (c) Use of funds Recipients of a grant under this section shall use the grant funds to\u2014 (1) deliver home-based telemental health services to covered populations; (2) develop comprehensive metrics to measure the quality and impact of home-based telemental health services compared to traditional in-person mental health and substance use care; and (3) support infrastructure that enhances the capacity of health care providers to deliver telemental health services in patients\u2019 homes or other places of comfort, including by\u2014 (A) expanding broadband access; (B) providing devices for patients to access telemental health services; and (C) offsetting costs of technology necessary for health care providers to deliver high quality care. (d) Report The Secretary, in consultation with the Secretary of Agriculture, not later than 3 years after the date on which the program under this section commences, and 2 years thereafter, shall submit to the appropriate congressional committees reports on the impact and quality of care of home-based telemental health care services for covered populations. (e) Authorized use of funds Out of any amounts made available to the Secretary, up to $10,000,000 for each of fiscal years 2025 through 2029 may be allocated to carrying out the program under this section. .",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-12-17",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6817",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Home-Based Telemental Health Care Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-04-04T14:03:31Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1056is.xml"
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
      "title": "Home-Based Telemental Health Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Home-Based Telemental Health Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a home-based telemental health care grant program for purposes of increasing mental health and substance use services in rural medically underserved populations and for individuals in farming, fishing, and forestry occupations",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:25Z"
    }
  ]
}
```
