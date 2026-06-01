# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6999?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6999
- Title: Tax Relief for Fraud Victims Act
- Congress: 119
- Bill type: HR
- Bill number: 6999
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-01-22T20:40:01Z
- Update date including text: 2026-01-22T20:40:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6999",
    "number": "6999",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Tax Relief for Fraud Victims Act",
    "type": "HR",
    "updateDate": "2026-01-22T20:40:01Z",
    "updateDateIncludingText": "2026-01-22T20:40:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
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
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
          "date": "2026-01-09T14:00:35Z",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6999ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6999\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mr. Miller of Ohio (for himself and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the limitation on deductions for personal casualty losses and to provide for increased taxpayer relief with respect to theft losses involving fraud, deceit, or misrepresentation.\n#### 1. Short title\nThis Act may be cited as the Tax Relief for Fraud Victims Act .\n#### 2. Repeal of limitation on deductions for personal casualty losses; increased taxpayer relief with respect to certain theft losses\n##### (a) Repeal of limitation on deductions for personal casualty losses\nSection 165(h) of the Internal Revenue Code of 1986 is amended by striking paragraph (5).\n##### (b) Certain theft losses sustained during taxable year of choice; extension of period of limitation for credit or refund claims for certain theft losses\n**(1) Certain theft losses sustained during taxable year of choice**\nSection 165(e) of such Code is amended to read as follows:\n(e) Theft losses For purposes of subsection (a)\u2014 (1) In general Except as provided in paragraph (2), any loss arising from theft shall be treated as sustained during the taxable year in which the taxpayer discovers such loss. (2) Theft losses involving fraud, deceit, or misrepresentation In the case of any loss arising from theft involving fraud, deceit, or misrepresentation (as defined by the Secretary), the taxpayer may elect to treat such loss as sustained during the taxable year in which such loss occurs. .\n**(2) Extension of period of limitation for credit or refund claims for certain theft losses**\nSection 165(h)(4) of such Code is amended by adding at the end the following new subparagraph:\n(F) Period of limitation for credit or refund claims for theft losses involving fraud, deceit, or misrepresentation In the case of a claim for credit or refund with respect to a deduction allowed under subsection (a) for any loss arising from theft involving fraud, deceit, or misrepresentation\u2014 (i) the period of limitation prescribed by section 6511(a) for the filing of such claim shall be treated as not expiring earlier than the date that is 1 year after the date on which the taxpayer discovers such loss, and (ii) section 6511(b)(2) shall not apply with respect to the filing of such claim. .\n##### (c) Distributions relating to theft losses involving fraud, deceit, or misrepresentation\nSection 72(t)(2) of such Code is amended by adding at the end the following new subparagraph:\n(O) Distributions relating to theft losses involving fraud, deceit, or misrepresentation (i) In general Any distribution to the extent it relates to any loss arising from theft involving fraud, deceit, or misrepresentation for which a deduction is allowed under section 165(a). (ii) Amount distributed may be repaid Rules similar to the rules of subparagraph (H)(v) shall apply with respect to an individual who receives a distribution to which clause (i) applies, except that subparagraph (H)(v)(I) shall be applied by substituting 1-year period beginning on the day after the date on which the taxpayer discovers the loss described in subparagraph (O)(i) for 3-year period beginning on the day after the date on which such distribution was received . (iii) Period of limitation for credit or refund claims In the case of a claim for credit or refund of the tax imposed by paragraph (1) with respect to a distribution described in clause (i)\u2014 (I) the period of limitation prescribed by section 6511(a) for the filing of such claim shall be treated as not expiring earlier than the date that is 1 year after the date on which the taxpayer discovers the loss described in clause (i), and (II) section 6511(b)(2) shall not apply with respect to the filing of such claim. .\n##### (d) Cross reference\nSection 6511(i) of such Code is amended by adding at the end the following new paragraph:\n(8) For a period of limitations for credit or refund in the case of theft losses involving fraud, deceit, or misrepresentation, see sections 72(t)(2)(O)(iii) and 165(h)(4)(F). .\n##### (e) Effective dates\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to losses sustained in taxable years beginning after December 31, 2025.\n**(2) Distributions relating to theft losses involving fraud, deceit, or misrepresentation**\nThe amendment made by subsection (c) shall apply to distributions made after December 31, 2025.",
      "versionDate": "2026-01-09",
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
        "updateDate": "2026-01-22T20:40:01Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6999ih.xml"
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
      "title": "Tax Relief for Fraud Victims Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Relief for Fraud Victims Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the limitation on deductions for personal casualty losses and to provide for increased taxpayer relief with respect to theft losses involving fraud, deceit, or misrepresentation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:48Z"
    }
  ]
}
```
