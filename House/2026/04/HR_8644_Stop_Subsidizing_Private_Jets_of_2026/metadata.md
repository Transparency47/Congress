# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8644?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8644
- Title: Stop Subsidizing Private Jets of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8644
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-13T15:53:49Z
- Update date including text: 2026-05-13T15:53:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8644",
    "number": "8644",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Stop Subsidizing Private Jets of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T15:53:49Z",
    "updateDateIncludingText": "2026-05-13T15:53:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8644ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8644\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Vindman (for himself, Ms. McDonald Rivet , and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to disallow deductions with respect to certain expenses relating to private planes.\n#### 1. Short title\nThis Act may be cited as the Stop Subsidizing Private Jets of 2026 .\n#### 2. Disallowance of certain expenses relating to private planes\n##### (a) in general\nSection 162 of the Internal Revenue Code of 1986 is amended by redesignating subsection (s) as subsection (t) and by inserting the following new subsection after subsection (r):\n(s) Disallowance of certain expenses relating to private planes (1) In general No deduction shall be allowed under this chapter for amounts paid or incurred for disqualified private plane expenditures. (2) Disqualified private plane expenditures For purposes of this subsection, the term disqualified private plane expenditures means amounts paid or incurred to purchase, maintain, or operate any fixed-wing aircraft (including any deduction for depreciation or amortization thereof) other than\u2014 (A) an aircraft\u2014 (i) an aircraft which is primarily used to transport property, or (ii) an aircraft which is modified for use in agriculture, firefighting, or for emergency medical purposes, and which is used by the taxpayer primarily for the purpose for which such aircraft has been modified, or (B) by a taxpayer in the course of a trade or business of the taxpayer\u2014 (i) of providing instruction in aeronautics, (ii) of offering skydiving services to the public, (iii) of offering transportation of persons by air along fixed and scheduled routes, if such services are predominately available for purchase by the general public, or (iv) of offering flights to the public for which the sole purpose is sightseeing. .\n##### (b) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after December 31, 2025.",
      "versionDate": "2026-04-30",
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
        "name": "Taxation",
        "updateDate": "2026-05-13T15:53:49Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8644ih.xml"
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
      "title": "Stop Subsidizing Private Jets of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Subsidizing Private Jets of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to disallow deductions with respect to certain expenses relating to private planes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:45Z"
    }
  ]
}
```
