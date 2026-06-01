# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/335
- Title: Rural Hospital Support Act
- Congress: 119
- Bill type: S
- Bill number: 335
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-07-17T11:03:18Z
- Update date including text: 2025-07-17T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/335",
    "number": "335",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Rural Hospital Support Act",
    "type": "S",
    "updateDate": "2025-07-17T11:03:18Z",
    "updateDateIncludingText": "2025-07-17T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
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
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T20:13:03Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "VT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "WV"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "VA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "NH"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "KS"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "MS"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "AR"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "AZ"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "MI"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s335is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 335\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Grassley (for himself, Mr. Welch , Mrs. Capito , Mr. Kaine , Mr. Wicker , Mrs. Shaheen , Mr. Moran , Ms. Smith , Mrs. Hyde-Smith , Mr. Fetterman , Mr. Boozman , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to rebase the calculation of payments for sole community hospitals and Medicare-dependent hospitals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Hospital Support Act .\n#### 2. Rebasing of the calculation of payments for sole community hospitals\n##### (a) Rebasing permitted\nSection 1886(b)(3) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3) ) is amended by adding at the end the following new subparagraph:\n(M) (i) For cost reporting periods beginning on or after October 1, 2025, in the case of a sole community hospital there shall be substituted for the amount otherwise determined under subsection (d)(5)(D)(i) of this section, if such substitution results in a greater amount of payment under this section for the hospital, the subparagraph (M) rebased target amount. (ii) For purposes of this subparagraph, the term subparagraph (M) rebased target amount has the meaning given the term target amount in subparagraph (C), except that\u2014 (I) there shall be substituted for the base cost reporting period the 12-month cost reporting period beginning during fiscal year 2016; (II) any reference in subparagraph (C)(i) to the first cost reporting period described in such subparagraph is deemed a reference to the first cost reporting period beginning on or after October 1, 2025; and (III) the applicable percentage increase shall only be applied under subparagraph (C)(iv) for discharges occurring on or after October 1, 2025. .\n##### (b) Conforming amendments\nSection 1886(b)(3) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (C), in the matter preceding clause (i), by striking subparagraphs (I) and (L) and inserting subparagraphs (I), (L), and (M) ; and\n**(2)**\nin subparagraph (I)(i), in the matter preceding subclause (I), by striking subparagraph (L) and inserting subparagraphs (L) and (M) .\n#### 3. Rebasing of the calculation of payments for Medicare-dependent hospitals\nSection 1886(b)(3) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3) ), as amended by section 2, is amended\u2014\n**(1)**\nin subparagraph (D), by striking subparagraph (K) and inserting subparagraphs (K) and (N) ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(N) (i) With respect to discharges occurring on or after October 1, 2025, in the case of a medicare-dependent, small rural hospital, for purposes of applying subparagraph (D)\u2014 (I) there shall be substituted for the base cost reporting period described in subparagraph (D)(i) the 12-month cost reporting period beginning during fiscal year 2016; and (II) any reference in such subparagraph to the first cost reporting period described in such subparagraph is deemed a reference to the first cost reporting period beginning on or after October 1, 2025. (ii) This subparagraph shall only apply to a hospital if the substitution described in clause (i)(I) results in an increase in the target amount under subparagraph (D) for the hospital. .\n#### 4. Prohibition of adjustments to classifications and weighting factors relating to the calculation of payments for sole community hospitals and Medicare-dependent hospitals\nSection 1886(d)(4)(C) of the Social Security Act ( 42 U.S.C. 1395ww(d)(4)(C) )\u2014\n**(1)**\nin clause (i), by striking The Secretary and inserting Subject to clause (v), the Secretary ; and\n**(2)**\nby adding at the end the following new clause:\n(v) For discharges using the rebased target amounts described in subparagraph (M) or (N) of subsection (b)(3), the Secretary may not adjust such amounts for adjustments required by clause (iii) prior to October 1, 2015. .\n#### 5. Extension of the medicare-dependent hospital (MDH) program\n##### (a) Extension of payment methodology\nSection 1886(d)(5)(G) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(G) ) is amended\u2014\n**(1)**\nin clause (i), by striking , and before April 1, 2025 ; and\n**(2)**\nin clause (ii)(II), by striking , and before April 1, 2025 .\n##### (b) Conforming amendments\n**(1) Extension of target amount**\nSection 1886(b)(3)(D) of the Social Security Act ( 42 U.S.C. 1395ww(b)(3)(D) ) is amended\u2014\n**(A)**\nin the matter preceding clause (i), by striking , and before April 1, 2025 ; and\n**(B)**\nin clause (iv), by striking through fiscal year 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting or a subsequent fiscal year .\n**(2) Permitting hospitals to decline reclassification**\nSection 13501(e)(2) of the Omnibus Budget Reconciliation Act of 1993 ( 42 U.S.C. 1395ww note) is amended by striking fiscal year 2000 through fiscal year 2024, or the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting a subsequent fiscal year .\n#### 6. Extension of the increased payments under the Medicare low-volume hospital program\nSection 1886(d)(12) of the Social Security Act ( 42 U.S.C. 1395(d)(12) ) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nin the subparagraph heading, by inserting for fiscal years 2005 through 2010 after increase ; and\n**(B)**\nin the matter preceding clause (i), by striking and for discharges occurring during the portion of fiscal year 2025 beginning on April 1, 2025, and ending on September 30, 2025, and in fiscal year 2026 and subsequent fiscal years ;\n**(2)**\nin subparagraph (C)(i)\u2014\n**(A)**\nin the matter preceding subclause (I), by striking fiscal years 2011 through 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting fiscal year 2011 and subsequent fiscal years ;\n**(B)**\nin subclause (III)\u2014\n**(i)**\nby striking each of fiscal years 2019 through 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting fiscal year 2019 and each subsequent fiscal year ; and\n**(ii)**\nby striking ; and at the end and inserting a period; and\n**(C)**\nby striking subclause (IV); and\n**(3)**\nin subparagraph (D)\u2014\n**(A)**\nby amending the subparagraph heading to reach as follows: Applicable percentage increase beginning with fiscal year 2011 .\u2014 ;\n**(B)**\nin the matter preceding clause (i), by striking fiscal years 2011 through 2024 or during the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting fiscal year 2011 and subsequent fiscal years ; and\n**(C)**\nin clause (ii), by striking each of fiscal years 2019 through 2024 and the portion of fiscal year 2025 beginning on October 1, 2024, and ending on March 31, 2025 and inserting fiscal year 2019 and each subsequent fiscal year .",
      "versionDate": "2025-01-30",
      "versionType": "Introduced in Senate"
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
            "name": "Health care coverage and access",
            "updateDate": "2025-04-04T19:30:54Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-04-04T19:30:54Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-04-04T19:30:54Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-04-04T19:30:54Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-04-04T19:30:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-07T15:18:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s335",
          "measure-number": "335",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s335v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Hospital Support Act</strong></p><p>This bill modifies and extends certain payment adjustments for rural hospitals under Medicare's inpatient prospective payment system.</p><p>Specifically, the bill indexes payment adjustments for sole community hospitals and Medicare-dependent hospitals to FY2016 operating costs, if it results in higher payments for such hospitals. The bill also makes payment adjustments for Medicare-dependent hospitals and low-volume hospitals permanent (the adjustments currently expire on March 31, 2025).</p>"
        },
        "title": "Rural Hospital Support Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s335.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Hospital Support Act</strong></p><p>This bill modifies and extends certain payment adjustments for rural hospitals under Medicare's inpatient prospective payment system.</p><p>Specifically, the bill indexes payment adjustments for sole community hospitals and Medicare-dependent hospitals to FY2016 operating costs, if it results in higher payments for such hospitals. The bill also makes payment adjustments for Medicare-dependent hospitals and low-volume hospitals permanent (the adjustments currently expire on March 31, 2025).</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119s335"
    },
    "title": "Rural Hospital Support Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Hospital Support Act</strong></p><p>This bill modifies and extends certain payment adjustments for rural hospitals under Medicare's inpatient prospective payment system.</p><p>Specifically, the bill indexes payment adjustments for sole community hospitals and Medicare-dependent hospitals to FY2016 operating costs, if it results in higher payments for such hospitals. The bill also makes payment adjustments for Medicare-dependent hospitals and low-volume hospitals permanent (the adjustments currently expire on March 31, 2025).</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119s335"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s335is.xml"
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
      "title": "Rural Hospital Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Hospital Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to rebase the calculation of payments for sole community hospitals and Medicare-dependent hospitals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:48Z"
    }
  ]
}
```
