# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/542
- Title: No Foreign Gifts Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 542
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-08-27T08:05:20Z
- Update date including text: 2025-08-27T08:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/542",
    "number": "542",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "No Foreign Gifts Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-27T08:05:20Z",
    "updateDateIncludingText": "2025-08-27T08:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:08:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr542ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 542\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Torres of New York (for himself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to prohibit institutions of higher education from receiving gifts from certain countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Foreign Gifts Act of 2025 .\n#### 2. Prohibition on gifts from certain countries\nThe Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ) is amended by inserting after section 117 the following:\n117A. Prohibition on gifts from certain countries (a) In general Beginning on the date of the enactment of this section, an institution of higher education that receives funds under this Act may not receive a gift from\u2014 (1) a country that, as of such date of enactment, has provided material support to a foreign terrorist organization, as determined by the Secretary of State; or (2) China, Russia, North Korea, or Iran. (b) Reporting In order to continue to be eligible to receive funds under this Act, an institution described in subsection (a) must, for each instance where such institution is offered a gift from a country described in such subsection, report such offer to the Secretary. (c) Definitions In this section: (1) Material support The term material support has the meaning given the term material support and resources in section 2339A(b) of title 18, United States Code. (2) Foreign terrorist organization The term foreign terrorist organization means an entity designated by the Secretary of State under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ). .",
      "versionDate": "2025-01-16",
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
            "name": "China",
            "updateDate": "2025-03-12T13:34:48Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-12T13:34:42Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-12T13:34:35Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-03-12T13:35:05Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-03-12T13:35:00Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-03-12T13:34:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-20T14:50:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr542",
          "measure-number": "542",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr542v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Foreign Gifts Act of 2025</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal education funds if the\u00a0IHE\u00a0receives gifts from certain countries.</p><p>Specifically, the bill prohibits an IHE from receiving a gift from (1) China, Russia, North Korea, or Iran; or (2) a country that has provided material support to a foreign terrorist organization, as determined by the Department of State.</p><p>The bill also requires an IHE, as a condition of eligibility for federal education funds, to report any offer of a gift from such a foreign country.</p>"
        },
        "title": "No Foreign Gifts Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr542.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Foreign Gifts Act of 2025</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal education funds if the\u00a0IHE\u00a0receives gifts from certain countries.</p><p>Specifically, the bill prohibits an IHE from receiving a gift from (1) China, Russia, North Korea, or Iran; or (2) a country that has provided material support to a foreign terrorist organization, as determined by the Department of State.</p><p>The bill also requires an IHE, as a condition of eligibility for federal education funds, to report any offer of a gift from such a foreign country.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr542"
    },
    "title": "No Foreign Gifts Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Foreign Gifts Act of 2025</strong></p><p>This bill prohibits an institution of higher education (IHE) from receiving federal education funds if the\u00a0IHE\u00a0receives gifts from certain countries.</p><p>Specifically, the bill prohibits an IHE from receiving a gift from (1) China, Russia, North Korea, or Iran; or (2) a country that has provided material support to a foreign terrorist organization, as determined by the Department of State.</p><p>The bill also requires an IHE, as a condition of eligibility for federal education funds, to report any offer of a gift from such a foreign country.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr542"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr542ih.xml"
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
      "title": "No Foreign Gifts Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T12:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Foreign Gifts Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to prohibit institutions of higher education from receiving gifts from certain countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T12:03:33Z"
    }
  ]
}
```
