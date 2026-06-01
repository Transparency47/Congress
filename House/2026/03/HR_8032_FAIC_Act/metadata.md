# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8032
- Title: FAIC Act
- Congress: 119
- Bill type: HR
- Bill number: 8032
- Origin chamber: House
- Introduced date: 2026-03-20
- Update date: 2026-05-20T08:06:42Z
- Update date including text: 2026-05-20T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-20: Introduced in House
- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-20: Introduced in House

## Actions

- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-20",
    "latestAction": {
      "actionDate": "2026-03-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8032",
    "number": "8032",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "FAIC Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:06:42Z",
    "updateDateIncludingText": "2026-05-20T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-20",
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
          "date": "2026-03-20T14:31:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-20T14:31:00Z",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NJ"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8032ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8032\nIN THE HOUSE OF REPRESENTATIVES\nMarch 20, 2026 Mr. Dunn of Florida (for himself and Mr. Soto ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to ensure equitable payment for, and preserve Medicare beneficiary access to, cancer treatments under the Medicare hospital outpatient prospective payment system.\n#### 1. Short title\nThis Act may be cited as the Facilitating Access to Innovation in Cancer Care Act or the FAIC Act .\n#### 2. Separate payment for certain cancer treatments\nSection 1833(t)(16) of the Social Security Act ( 42 U.S.C. 1395(t)(16) ) is amended by adding at the end the following new subparagraph:\n(H) Separate payment for certain cancer treatments (i) In general Notwithstanding any other provision of this subsection, with respect to a specified cancer treatment (as defined in clause (v)) furnished during a year (beginning with 2026), the Secretary shall not package payment for such treatment into a payment for a covered OPD service (or group of services), and shall make a separate payment as specified in clause (ii) for such treatment, if such treatment has an estimated mean per day product cost equal to or exceeding the threshold specified in clause (iii) for such year. (ii) Separate payment For purposes of clause (i), the separate payment specified in this clause for a specified cancer treatment is a payment in an amount equal to\u2014 (I) the average sales price for such treatment established under section 1847A, as calculated and adjusted by the Secretary to the extent such adjustment is adopted for other specified covered outpatient drugs under paragraph (14)(A)(iii)(II); or (II) if the data necessary to calculate such average sales price for such treatment is not available, the wholesale acquisition cost (as defined in subsection 1847A(c)(6)(B)) for such treatment, as calculated and adjusted by the Secretary to the extent such adjustment is adopted for other specified covered outpatient drugs under paragraph (14)(A), or, if such wholesale acquisition cost is not available, the mean unit cost for such treatment (as derived from hospital claims data). (iii) Threshold For purposes of clause (i), the threshold specified in this clause is\u2014 (I) for 2026, $350; and (II) for a subsequent year, the amount specified in this clause for the preceding year, increased by the OPD fee schedule increase factor under paragraph (3)(C)(iv) for the year. (iv) Budget neutrality The Secretary shall make such adjustments as are necessary under this subsection to ensure that the amount of expenditures under this subsection for a year with application of this subparagraph is equal to the amount of expenditures that would be made under this subsection for such year without application of this subparagraph. (v) Definition For purposes of this subparagraph, the term specified cancer treatment means a drug or biological that\u2014 (I) is approved by the Food and Drug Administration on or after January 1, 2008, for use in the detection or treatment of cancer; (II) does not receive transitional pass-through payments under paragraph (6); and (III) has payment that would, but for application of this subparagraph, be packaged into a payment for a covered OPD service (or group of services). .",
      "versionDate": "2026-03-20",
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
        "updateDate": "2026-04-09T20:02:59Z"
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
      "date": "2026-03-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8032ih.xml"
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
      "title": "FAIC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Facilitating Access to Innovation in Cancer Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to ensure equitable payment for, and preserve Medicare beneficiary access to, cancer treatments under the Medicare hospital outpatient prospective payment system.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:27Z"
    }
  ]
}
```
