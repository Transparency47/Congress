# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/207?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/207
- Title: Protecting Life on College Campus Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 207
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/207",
    "number": "207",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Protecting Life on College Campus Act of 2025",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T17:47:18Z",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ND"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AR"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NE"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s207is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 207\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Daines (for himself, Mr. Lankford , Mr. Risch , Mr. Cramer , Mr. Budd , Mr. Banks , Mr. Boozman , Mrs. Hyde-Smith , Mrs. Britt , Mr. Wicker , Mrs. Fischer , Mr. Hawley , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit the award of Federal funds to an institution of higher education that hosts or is affiliated with a student-based service site that provides abortion drugs or abortions to students of the institution or to employees of the institution or site, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Life on College Campus Act of 2025 .\n#### 2. Prohibition on award of funds to certain institutions of higher education\n##### (a) Prohibition\nNo Federal funds may be awarded (directly or indirectly, including through a contract or subcontract) to any institution of higher education that hosts or is affiliated with any school-based service site that provides abortion drugs or abortions to students of such institution or to employees of such institution or site.\n##### (b) Annual reporting\nTo remain eligible for awards of Federal funds, an institution of higher education that hosts or is affiliated with one or more school-based service sites shall submit an annual report to the Secretary of Education and the Secretary of Health and Human Services certifying that no such site provides abortion drugs or abortions to students of the institution or to employees of such institution or site.\n##### (c) Preemption\nAn institution of higher education that receives Federal funds may not be subject to any penalty under State law solely by reason of compliance with this section.\n##### (d) Definitions\nIn this section:\n**(1) Abortion drug**\nThe term abortion drug means any drug, substance, or combination of drugs or substances that is intended for use or that is in fact used (irrespective of how the product is labeled)\u2014\n**(A)**\nto intentionally kill the unborn child of a woman known to be pregnant; or\n**(B)**\nto intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014\n**(i)**\nto produce a live birth;\n**(ii)**\nto remove a dead unborn child; or\n**(iii)**\nto treat an ectopic pregnancy.\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ).\n**(3) School-based service site**\nThe term school-based service site \u2014\n**(A)**\nmeans a clinic providing health care services (including primary health services, family planning services, telehealth services, and pharmaceutical services, without regard to whether the services are provided by employees of the clinic or contracted providers) to students that is located on the campus of an institution of higher education that accepts Federal funding; and\n**(B)**\ndoes not include a hospital (as defined in section 1861(e) of the Social Security Act ( 42 U.S.C. 1395x(e) )).",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "632",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Life on College Campus Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-03-19T15:10:12Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-19T15:10:12Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-19T15:10:12Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-19T15:10:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-01T14:19:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s207",
          "measure-number": "207",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s207v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Life on College Campus Act of </strong><strong>2025</strong></p><p>This bill prohibits the award of federal funds to an institution of higher education (IHE) that hosts or is affiliated with a school-based service site that provides abortion drugs or abortions to its students or to employees of the IHE or the site. An IHE that hosts or is affiliated with a site must, in order to remain eligible for federal funds, annually certify that the site does not provide abortion drugs or abortions to students or employees.</p>"
        },
        "title": "Protecting Life on College Campus Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s207.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life on College Campus Act of </strong><strong>2025</strong></p><p>This bill prohibits the award of federal funds to an institution of higher education (IHE) that hosts or is affiliated with a school-based service site that provides abortion drugs or abortions to its students or to employees of the IHE or the site. An IHE that hosts or is affiliated with a site must, in order to remain eligible for federal funds, annually certify that the site does not provide abortion drugs or abortions to students or employees.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s207"
    },
    "title": "Protecting Life on College Campus Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life on College Campus Act of </strong><strong>2025</strong></p><p>This bill prohibits the award of federal funds to an institution of higher education (IHE) that hosts or is affiliated with a school-based service site that provides abortion drugs or abortions to its students or to employees of the IHE or the site. An IHE that hosts or is affiliated with a site must, in order to remain eligible for federal funds, annually certify that the site does not provide abortion drugs or abortions to students or employees.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s207"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s207is.xml"
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
      "title": "Protecting Life on College Campus Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Life on College Campus Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the award of Federal funds to an institution of higher education that hosts or is affiliated with a student-based service site that provides abortion drugs or abortions to students of the institution or to employees of the institution or site, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:19Z"
    }
  ]
}
```
