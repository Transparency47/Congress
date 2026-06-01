# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/329?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/329
- Title: Expanding Penalty Free Withdrawal Act
- Congress: 119
- Bill type: HR
- Bill number: 329
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-03-18T18:45:44Z
- Update date including text: 2025-03-18T18:45:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/329",
    "number": "329",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Expanding Penalty Free Withdrawal Act",
    "type": "HR",
    "updateDate": "2025-03-18T18:45:44Z",
    "updateDateIncludingText": "2025-03-18T18:45:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:32:50Z",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "DC"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr329ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 329\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mrs. Watson Coleman (for herself, Mrs. Cherfilus-McCormick , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the availability of penalty-free distributions to unemployed individuals from retirement plans.\n#### 1. Short title\nThis Act may be cited as the Expanding Penalty Free Withdrawal Act .\n#### 2. Expansion of exception for penalty on early distributions to unemployed individuals from retirement plans\n##### (a) In general\nSection 72(t)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(N) Long-term unemployment distributions (i) In general Distributions to an individual after separation from employment\u2014 (I) if such individual has received unemployment compensation for 26 consecutive weeks under any Federal or State unemployment compensation law by reason of such separation (or, if less, for the maximum period for which unemployment compensation is available under State law applicable to the individual), and (II) if such distributions are made during any taxable year during which such unemployment compensation is paid or the succeeding taxable year. (ii) Distributions after reemployment; self-employed individuals Rules similar to the rules of clauses (ii) and (iii) of subparagraph (D) shall apply for purposes of this subparagraph. (iii) Limitation Clause (i) shall not apply to any distribution to the extent that such distribution exceeds the lesser of\u2014 (I) $50,000, reduced by the aggregate amount of distributions which are described in clause (i) from all plans of the individual during the 1-year period ending on the day before the date on which such distribution was made, or (II) the greater of $10,000 or one-half of the aggregate fair market value (at the time of the distribution) of the individual\u2019s qualified retirement plans (as defined in section 4974(c)) and the nonforfeitable portion the individual\u2019s defined contribution plans. (iv) Coordination with distributions to unemployed individuals for health insurance premiums Distributions shall not be taken into account under this subparagraph if such distributions are described in subparagraph (D). .\n##### (b) Effective date\nThe amendments made by this section shall apply to distributions made after December 31, 2024.",
      "versionDate": "2025-01-09",
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
            "name": "Employee benefits and pensions",
            "updateDate": "2025-03-18T18:45:14Z"
          },
          {
            "name": "Income tax deferral",
            "updateDate": "2025-03-18T18:45:21Z"
          },
          {
            "name": "Income tax exclusion",
            "updateDate": "2025-03-18T18:45:30Z"
          },
          {
            "name": "Income tax rates",
            "updateDate": "2025-03-18T18:45:38Z"
          },
          {
            "name": "Unemployment",
            "updateDate": "2025-03-18T18:45:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-14T16:42:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr329",
          "measure-number": "329",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr329v00",
            "update-date": "2025-02-24"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expanding Penalty Free Withdrawal Act</strong></p><p>This bill allows an individual who is unemployed for a certain period of time to take early distributions from a qualified retirement plan without paying an additional tax on such distributions, subject to limitations.</p><p>Under current law, a 10% additional tax is imposed on early distributions from a qualified retirement plan unless an exception applies.\u00a0</p><p>This bill expands the list of exceptions to include distributions from a qualified retirement plan made (1) to an individual who is unemployed and receives federal or state unemployment compensation for 26 consecutive weeks (or the maximum number of weeks allowed under state law) and (2) in the same tax year that the unemployment compensation is paid or the following tax year.\u00a0However, under the bill, the 10% additional tax applies to distributions from a qualified retirement plan made after an individual is employed for at least 60 days following a period of unemployment.</p><p>The bill limits the amount that may be distributed to an unemployed individual from a qualified retirement plan free from the 10% additional tax to the lesser of (1) $50,000 in distributions from all of an individual\u2019s qualified plans over a one-year period, or (2) the greater of $10,000 or half the fair market value of an individual\u2019s qualified retirement plans and the nonforfeitable portion of an individual's defined contribution plans.</p><p>\u00a0</p>"
        },
        "title": "Expanding Penalty Free Withdrawal Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr329.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Penalty Free Withdrawal Act</strong></p><p>This bill allows an individual who is unemployed for a certain period of time to take early distributions from a qualified retirement plan without paying an additional tax on such distributions, subject to limitations.</p><p>Under current law, a 10% additional tax is imposed on early distributions from a qualified retirement plan unless an exception applies.\u00a0</p><p>This bill expands the list of exceptions to include distributions from a qualified retirement plan made (1) to an individual who is unemployed and receives federal or state unemployment compensation for 26 consecutive weeks (or the maximum number of weeks allowed under state law) and (2) in the same tax year that the unemployment compensation is paid or the following tax year.\u00a0However, under the bill, the 10% additional tax applies to distributions from a qualified retirement plan made after an individual is employed for at least 60 days following a period of unemployment.</p><p>The bill limits the amount that may be distributed to an unemployed individual from a qualified retirement plan free from the 10% additional tax to the lesser of (1) $50,000 in distributions from all of an individual\u2019s qualified plans over a one-year period, or (2) the greater of $10,000 or half the fair market value of an individual\u2019s qualified retirement plans and the nonforfeitable portion of an individual's defined contribution plans.</p><p>\u00a0</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr329"
    },
    "title": "Expanding Penalty Free Withdrawal Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Penalty Free Withdrawal Act</strong></p><p>This bill allows an individual who is unemployed for a certain period of time to take early distributions from a qualified retirement plan without paying an additional tax on such distributions, subject to limitations.</p><p>Under current law, a 10% additional tax is imposed on early distributions from a qualified retirement plan unless an exception applies.\u00a0</p><p>This bill expands the list of exceptions to include distributions from a qualified retirement plan made (1) to an individual who is unemployed and receives federal or state unemployment compensation for 26 consecutive weeks (or the maximum number of weeks allowed under state law) and (2) in the same tax year that the unemployment compensation is paid or the following tax year.\u00a0However, under the bill, the 10% additional tax applies to distributions from a qualified retirement plan made after an individual is employed for at least 60 days following a period of unemployment.</p><p>The bill limits the amount that may be distributed to an unemployed individual from a qualified retirement plan free from the 10% additional tax to the lesser of (1) $50,000 in distributions from all of an individual\u2019s qualified plans over a one-year period, or (2) the greater of $10,000 or half the fair market value of an individual\u2019s qualified retirement plans and the nonforfeitable portion of an individual's defined contribution plans.</p><p>\u00a0</p>",
      "updateDate": "2025-02-24",
      "versionCode": "id119hr329"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr329ih.xml"
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
      "title": "Expanding Penalty Free Withdrawal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Penalty Free Withdrawal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the availability of penalty-free distributions to unemployed individuals from retirement plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:28Z"
    }
  ]
}
```
