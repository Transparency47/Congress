# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1973?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1973
- Title: Treat and Reduce Obesity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1973
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-02-24T12:03:19Z
- Update date including text: 2026-02-24T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1973",
    "number": "1973",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Treat and Reduce Obesity Act of 2025",
    "type": "S",
    "updateDate": "2026-02-24T12:03:19Z",
    "updateDateIncludingText": "2026-02-24T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
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
        "item": [
          {
            "date": "2025-06-05T17:39:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-05T17:39:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NM"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "PA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "AZ"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "MS"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "MS"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MN"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NM"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NH"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NC"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "MD"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1973is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1973\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Cassidy (for himself, Mr. Luj\u00e1n , Mr. Tillis , Mr. Padilla , Mrs. Blackburn , Mr. Fetterman , Mrs. Capito , Mr. Gallego , Mrs. Hyde-Smith , Mr. Peters , Mr. Wicker , Ms. Klobuchar , Mr. Booker , Mr. Blumenthal , Mr. Heinrich , Mr. Van Hollen , Mr. Coons , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for the coordination of programs to prevent and treat obesity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Treat and Reduce Obesity Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nAccording to the Centers for Disease Control and Prevention, about 41 percent of adults aged 60 and over had obesity in the period of 2015 through 2016, representing more than 27,000,000 people.\n**(2)**\nThe National Institutes of Health has reported that obesity and overweight are now the second leading cause of death nationally, with an estimated 300,000 deaths a year attributed to the epidemic.\n**(3)**\nObesity increases the risk for chronic diseases and conditions, including high blood pressure, heart disease, certain cancers, arthritis, mental illness, lipid disorders, sleep apnea, and type 2 diabetes.\n**(4)**\nMore than half of Medicare beneficiaries are treated for 5 or more chronic conditions per year. The rate of obesity among Medicare beneficiaries doubled from 1987 to 2002, and nearly doubled again by 2016, with Medicare spending on individuals with obesity during that time rising proportionately to reach $50,000,000,000 in 2014.\n**(5)**\nMen and women with obesity at age 65 have decreased life expectancy of 1.6 years for men and 1.4 years for women.\n**(6)**\nThe direct and indirect cost of obesity was more than $427,800,000,000 in 2014, and is growing.\n**(7)**\nOn average, a Medicare beneficiary with obesity costs $2,018 (in 2019 dollars) more than a healthy-weight beneficiary.\n**(8)**\nThe prevalence of obesity among older individuals in the United States is growing at a linear rate and, if nothing changes, nearly one in two (47 percent) Medicare beneficiaries aged 65 and over will have obesity in 2030, up from slightly more than one in four (28 percent) in 2010.\n#### 3. Authority to expand health care providers qualified to furnish intensive behavioral therapy\nSection 1861(ddd) of the Social Security Act ( 42 U.S.C. 1395x(ddd) ) is amended by adding at the end the following new paragraph:\n(4) (A) Subject to subparagraph (B), the Secretary may, in addition to qualified primary care physicians and other primary care practitioners, cover intensive behavioral therapy for obesity furnished by any of the following: (i) A physician (as defined in subsection (r)(1)) who is not a qualified primary care physician. (ii) Any other appropriate health care provider (including a physician assistant, nurse practitioner, or clinical nurse specialist (as those terms are defined in subsection (aa)(5)), a clinical psychologist, a registered dietitian or nutrition professional (as defined in subsection (vv))). (iii) An evidence-based, community-based lifestyle counseling program approved by the Secretary. (B) In the case of intensive behavioral therapy for obesity furnished by a provider described in clause (ii) or (iii) of subparagraph (A), the Secretary may only cover such therapy if such therapy is furnished\u2014 (i) upon referral from, and in coordination with, a physician or primary care practitioner operating in a primary care setting or any other setting specified by the Secretary; and (ii) in an office setting, a hospital outpatient department, a community-based site that complies with the Federal regulations concerning the privacy of individually identifiable health information promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996, or another setting specified by the Secretary. (C) In order to ensure a collaborative effort, the coordination described in subparagraph (B)(i) shall include the health care provider or lifestyle counseling program communicating to the referring physician or primary care practitioner any recommendations or treatment plans made regarding the therapy. .\n#### 4. Medicare part D coverage of obesity medication\n##### (a) In general\nSection 1860D\u20132(e)(2)(A) of the Social Security Act ( 42 U.S.C. 1395w\u2013102(e)(2)(A) ) is amended, in the first sentence\u2014\n**(1)**\nby striking and other than and inserting other than ; and\n**(2)**\nby inserting after benzodiazepines), the following: and other than subparagraph (A) of such section if the drug is used for the treatment of obesity (as defined in section 1861(yy)(2)(C)) or for weight loss management for an individual who is overweight (as defined in section 1861(yy)(2)(F)(i)) and has one or more related comorbidities, .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to plan years beginning on or after the date that is 2 years after the date of the enactment of this Act.\n#### 5. Report to Congress\nNot later than the date that is 1 year after the date of the enactment of this Act, and every 2 years thereafter, the Secretary of Health and Human Services shall submit a report to Congress describing the steps the Secretary has taken to implement the provisions of, and amendments made by, this Act. Such report shall also include recommendations for better coordination and leveraging of programs within the Department of Health and Human Services and other Federal agencies that relate in any way to supporting appropriate research and clinical care (such as any interactions between physicians and other health care providers and their patients) to treat, reduce, and prevent obesity in the adult population.",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-06-27",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4231",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Treat and Reduce Obesity Act of 2025",
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
        "updateDate": "2026-01-09T12:13:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
    "originChamber": "Senate",
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
          "measure-id": "id119s1973",
          "measure-number": "1973",
          "measure-type": "s",
          "orig-publish-date": "2025-06-05",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1973v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Treat and Reduce Obesity Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of intensive behavioral therapy for obesity. Specifically, the bill allows coverage for therapy that is provided by (1) a physician who is not a primary care physician; or\u00a0(2) other health care providers (e.g., physician assistants and nurse practitioners) and approved counseling programs, if provided upon a referral from, and in coordination with, a physician or primary care practitioner. Currently, such therapy is covered only if provided by a primary care practitioner.</p><p>The bill also allows coverage under Medicare's prescription drug benefit of drugs used for the treatment of obesity or for weight loss management for individuals who are overweight.</p>"
        },
        "title": "Treat and Reduce Obesity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1973.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Treat and Reduce Obesity Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of intensive behavioral therapy for obesity. Specifically, the bill allows coverage for therapy that is provided by (1) a physician who is not a primary care physician; or\u00a0(2) other health care providers (e.g., physician assistants and nurse practitioners) and approved counseling programs, if provided upon a referral from, and in coordination with, a physician or primary care practitioner. Currently, such therapy is covered only if provided by a primary care practitioner.</p><p>The bill also allows coverage under Medicare's prescription drug benefit of drugs used for the treatment of obesity or for weight loss management for individuals who are overweight.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1973"
    },
    "title": "Treat and Reduce Obesity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Treat and Reduce Obesity Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of intensive behavioral therapy for obesity. Specifically, the bill allows coverage for therapy that is provided by (1) a physician who is not a primary care physician; or\u00a0(2) other health care providers (e.g., physician assistants and nurse practitioners) and approved counseling programs, if provided upon a referral from, and in coordination with, a physician or primary care practitioner. Currently, such therapy is covered only if provided by a primary care practitioner.</p><p>The bill also allows coverage under Medicare's prescription drug benefit of drugs used for the treatment of obesity or for weight loss management for individuals who are overweight.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1973"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1973is.xml"
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
      "title": "Treat and Reduce Obesity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Treat and Reduce Obesity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for the coordination of programs to prevent and treat obesity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:44Z"
    }
  ]
}
```
