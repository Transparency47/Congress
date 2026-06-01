# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1298?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1298
- Title: Religious Workforce Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1298
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-02-14T00:14:23Z
- Update date including text: 2026-02-14T00:14:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1298",
    "number": "1298",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Religious Workforce Protection Act",
    "type": "S",
    "updateDate": "2026-02-14T00:14:23Z",
    "updateDateIncludingText": "2026-02-14T00:14:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T21:38:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "ME"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "ID"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "DE"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AK"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "ID"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1298is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1298\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Kaine (for himself, Ms. Collins , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize the continuation of lawful nonimmigrant status for certain religious workers affected by the backlog for religious worker immigrant visas.\n#### 1. Short title\nThis Act may be cited as the Religious Workforce Protection Act .\n#### 2. Extension of nonimmigrant status for religious workers caught in long backlogs for lawful permanent residence\n##### (a) In general\nSection 214(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1184(a)(2) ) is amended by adding at the end the following:\n(C) Notwithstanding section 101(a)(15)(R)(ii), an alien may apply for, and the Secretary of Homeland Security may grant, an extension of nonimmigrant status under section 101(a)(15)(R) until such alien\u2019s application for adjustment of status or an immigrant visa has been processed and a decision has been made on such application if the alien\u2014 (i) is the principal or derivative beneficiary of an immigrant petition filed pursuant to section 204(a) for a preference status under section 203(b)(4); and (ii) is eligible to be granted such immigrant status absent the application of the numerical limitations under sections 201, 202, and 203. .\n##### (b) Conforming amendment\nSection 101(a)(15)(R)(ii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(R)(ii) ) is amended by inserting , except as provided in section 214(a)(2)(C), after 5 years .\n#### 3. Limited job flexibility for certain religious workers with long-delayed applications for lawful permanent residence\nSection 204(j) of the Immigration and Nationality Act ( 8 U.S.C. 1154(j) ) is amended by striking subsection (a)(1)(D) and inserting subsection (a)(1)(F) or subsection (a)(1)(G)(i) (with respect to special immigrants described in section 101(a)(27)(C)) .\n#### 4. Exemption to 1-year foreign residence requirement for certain nonimmigrant religious workers\nAn alien described in section 214(a)(2)(C) of the Immigration and Nationality Act, as added by section 2(a), who departed from the United States due to the 5-year limitation on nonimmigrant status under section 101(a)(15)(R) of such Act ( 8 U.S.C. 1101(a)(15)(R) ) shall be exempt from the 1-year foreign residence requirement set forth in section 214.2(r)(6) of title 8, Code of Federal Regulations.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2672",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Religious Workforce Protection Act",
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
        "name": "Immigration",
        "updateDate": "2025-05-05T12:25:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119s1298",
          "measure-number": "1298",
          "measure-type": "s",
          "orig-publish-date": "2025-04-03",
          "originChamber": "SENATE",
          "update-date": "2026-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1298v00",
            "update-date": "2026-02-14"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Religious Workforce Protection Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) to extend the nonimmigrant visa status of certain religious workers.</p><p>Under current law, if specified conditions are met, nonimmigrant religious workers may receive a visa for a period not to exceed five years. The bill allows\u00a0DHS to grant an extension until the individual\u2019s application for adjustment of status to permanent resident or an immigrant visa has been processed and a decision has been made. To be eligible for the extension, the individual must be (1) the beneficiary of a certain type of immigrant petition, and (2) eligible for such immigrant status\u00a0absent the application of certain numerical limitations.</p><p>Such individuals who have pending adjustment of status applications are also granted certain job\u00a0flexibilities, such as the ability to change employers. Individuals who have previously departed the U.S. due to the expiration of their visa are exempt from the one-year foreign residence requirement to renew their visa.</p>"
        },
        "title": "Religious Workforce Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1298.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Religious Workforce Protection Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) to extend the nonimmigrant visa status of certain religious workers.</p><p>Under current law, if specified conditions are met, nonimmigrant religious workers may receive a visa for a period not to exceed five years. The bill allows\u00a0DHS to grant an extension until the individual\u2019s application for adjustment of status to permanent resident or an immigrant visa has been processed and a decision has been made. To be eligible for the extension, the individual must be (1) the beneficiary of a certain type of immigrant petition, and (2) eligible for such immigrant status\u00a0absent the application of certain numerical limitations.</p><p>Such individuals who have pending adjustment of status applications are also granted certain job\u00a0flexibilities, such as the ability to change employers. Individuals who have previously departed the U.S. due to the expiration of their visa are exempt from the one-year foreign residence requirement to renew their visa.</p>",
      "updateDate": "2026-02-14",
      "versionCode": "id119s1298"
    },
    "title": "Religious Workforce Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Religious Workforce Protection Act</strong></p><p>This bill allows the Department of Homeland Security (DHS) to extend the nonimmigrant visa status of certain religious workers.</p><p>Under current law, if specified conditions are met, nonimmigrant religious workers may receive a visa for a period not to exceed five years. The bill allows\u00a0DHS to grant an extension until the individual\u2019s application for adjustment of status to permanent resident or an immigrant visa has been processed and a decision has been made. To be eligible for the extension, the individual must be (1) the beneficiary of a certain type of immigrant petition, and (2) eligible for such immigrant status\u00a0absent the application of certain numerical limitations.</p><p>Such individuals who have pending adjustment of status applications are also granted certain job\u00a0flexibilities, such as the ability to change employers. Individuals who have previously departed the U.S. due to the expiration of their visa are exempt from the one-year foreign residence requirement to renew their visa.</p>",
      "updateDate": "2026-02-14",
      "versionCode": "id119s1298"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1298is.xml"
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
      "title": "Religious Workforce Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Religious Workforce Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the continuation of lawful nonimmigrant status for certain religious workers affected by the backlog for religious worker immigrant visas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:26Z"
    }
  ]
}
```
