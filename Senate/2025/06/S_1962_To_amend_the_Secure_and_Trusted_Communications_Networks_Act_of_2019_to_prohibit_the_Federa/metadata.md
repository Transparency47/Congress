# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1962
- Title: Secure Space Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1962
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-05-27T15:20:27Z
- Update date including text: 2026-05-27T15:20:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-04-14 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1962",
    "number": "1962",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Secure Space Act of 2025",
    "type": "S",
    "updateDate": "2026-05-27T15:20:27Z",
    "updateDateIncludingText": "2026-05-27T15:20:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
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
            "date": "2026-04-14T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-05T14:49:23Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1962is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1962\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mrs. Fischer (for herself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Secure and Trusted Communications Networks Act of 2019 to prohibit the Federal Communications Commission from granting a license or United States market access for a geostationary orbit satellite system or a nongeostationary orbit satellite system, or an authorization to use an individually licensed earth station or a blanket-licensed earth station, if the license, grant of market access, or authorization would be held or controlled by an entity that produces or provides any covered communications equipment or service or an affiliate of such an entity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Space Act of 2025 .\n#### 2. Prohibition on grant of certain satellite licenses, United States market access, or earth station authorizations\n##### (a) In general\nThe Secure and Trusted Communications Networks Act of 2019 ( 47 U.S.C. 1601 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 10 and 11 as sections 11 and 12, respectively; and\n**(2)**\nby inserting after section 9 the following:\n10. Prohibition on grant of certain satellite licenses, United States market access, or earth station authorizations (a) Definitions In this section: (1) Affiliate (A) In general The term affiliate means an entity that (directly or indirectly) owns or controls, is owned or controlled by, or is under common ownership or control with, another entity. (B) Own For purposes of this paragraph, the term own means to have, possess, or otherwise control an equity interest (or the equivalent thereof) of not less than 10 percent. (2) Blanket-licensed earth station The term blanket-licensed earth station means an earth station that is licensed with a geostationary orbit satellite system or a nongeostationary orbit satellite system. (3) Gateway station The term gateway station means an earth station or a group of earth stations that\u2014 (A) supports the routing and switching functions of a geostationary orbit satellite system or a nongeostationary orbit satellite system; (B) may also be used for telemetry, tracking, and command transmissions; (C) does not originate or terminate communication traffic; and (D) is not for the exclusive use of any customer. (4) Individually licensed earth station The term individually licensed earth station means\u2014 (A) an earth station (other than a blanket-licensed earth station) that sends a signal to, and receives a signal from, a geostationary orbit satellite system or a nongeostationary orbit satellite system; or (B) a gateway station. (b) Prohibition The Commission may not grant a license for, or a petition for a declaratory ruling to access the United States market using, a geostationary orbit satellite system or a nongeostationary orbit satellite system, or an authorization to use an individually licensed earth station or a blanket-licensed earth station, if the license, grant of market access, or authorization would be held or controlled by\u2014 (1) an entity that produces or provides any covered communications equipment or service; or (2) an affiliate of an entity described in paragraph (1). .\n##### (b) Applicability\nSection 10 of the Secure and Trusted Communications Networks Act of 2019, as added by subsection (a), shall apply with respect to the grant of a license, petition, or authorization on or after the date of enactment of this Act.\n##### (c) Rules\nNot later than 1 year after the date of enactment of this Act, the Federal Communications Commission shall issue rules to implement section 10 of the Secure and Trusted Communications Networks Act of 2019, as added by subsection (a).",
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
        "actionDate": "2025-04-29",
        "text": "Received in the Senate and Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2458",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Secure Space Act of 2025",
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
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2026-04-15T20:29:43Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-04-15T20:29:43Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-04-15T20:29:43Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2026-04-15T20:29:43Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-04-15T20:29:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-06-25T12:55:40Z"
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
          "measure-id": "id119s1962",
          "measure-number": "1962",
          "measure-type": "s",
          "orig-publish-date": "2025-06-05",
          "originChamber": "SENATE",
          "update-date": "2026-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1962v00",
            "update-date": "2026-02-27"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Secure Space Act of 2025</strong></p><p>This bill prohibits the Federal Communications Commission (FCC) from granting satellite licenses or earth station authorizations, including U.S. market access for foreign-licensed satellites, to specified foreign entities of concern and their affiliates. (Earth stations, also commonly known as ground stations, are earth-based radio stations that communicate with satellites. A grant of U.S. market access permits one or more foreign-licensed satellites to communicate with one or more U.S.-licensed earth stations.)</p><p>Specifically, the FCC may not grant a satellite license, an earth station authorization, or market access to any entity, or an affiliate thereof, that produces or provides communications equipment or services deemed to pose an unacceptable risk to the national security of the United States. (The FCC maintains a list of such equipment and services, known as the Covered List. Providers of such equipment and services include, for example, Huawei Technologies Company and ZTE Corporation.)\u00a0</p>"
        },
        "title": "Secure Space Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1962.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Secure Space Act of 2025</strong></p><p>This bill prohibits the Federal Communications Commission (FCC) from granting satellite licenses or earth station authorizations, including U.S. market access for foreign-licensed satellites, to specified foreign entities of concern and their affiliates. (Earth stations, also commonly known as ground stations, are earth-based radio stations that communicate with satellites. A grant of U.S. market access permits one or more foreign-licensed satellites to communicate with one or more U.S.-licensed earth stations.)</p><p>Specifically, the FCC may not grant a satellite license, an earth station authorization, or market access to any entity, or an affiliate thereof, that produces or provides communications equipment or services deemed to pose an unacceptable risk to the national security of the United States. (The FCC maintains a list of such equipment and services, known as the Covered List. Providers of such equipment and services include, for example, Huawei Technologies Company and ZTE Corporation.)\u00a0</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s1962"
    },
    "title": "Secure Space Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Secure Space Act of 2025</strong></p><p>This bill prohibits the Federal Communications Commission (FCC) from granting satellite licenses or earth station authorizations, including U.S. market access for foreign-licensed satellites, to specified foreign entities of concern and their affiliates. (Earth stations, also commonly known as ground stations, are earth-based radio stations that communicate with satellites. A grant of U.S. market access permits one or more foreign-licensed satellites to communicate with one or more U.S.-licensed earth stations.)</p><p>Specifically, the FCC may not grant a satellite license, an earth station authorization, or market access to any entity, or an affiliate thereof, that produces or provides communications equipment or services deemed to pose an unacceptable risk to the national security of the United States. (The FCC maintains a list of such equipment and services, known as the Covered List. Providers of such equipment and services include, for example, Huawei Technologies Company and ZTE Corporation.)\u00a0</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s1962"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1962is.xml"
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
      "title": "Secure Space Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure Space Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Secure and Trusted Communications Networks Act of 2019 to prohibit the Federal Communications Commission from granting a license or United States market access for a geostationary orbit satellite system or a nongeostationary orbit satellite system, or an authorization to use an individually licensed earth station or a blanket-licensed earth station, if the license, grant of market access, or authorization would be held or controlled by an entity that produces or provides any covered communications equipment or service or an affiliate of such an entity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T05:33:20Z"
    }
  ]
}
```
