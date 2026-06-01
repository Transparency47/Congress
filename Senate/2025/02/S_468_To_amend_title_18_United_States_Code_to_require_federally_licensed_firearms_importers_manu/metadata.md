# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/468
- Title: SECURE Firearm Storage Act
- Congress: 119
- Bill type: S
- Bill number: 468
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-05T21:47:19Z
- Update date including text: 2025-12-05T21:47:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S795)
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S795)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/468",
    "number": "468",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "SECURE Firearm Storage Act",
    "type": "S",
    "updateDate": "2025-12-05T21:47:19Z",
    "updateDateIncludingText": "2025-12-05T21:47:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S795)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T19:52:23Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MN"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s468is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 468\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Durbin (for himself, Mr. Blumenthal , Ms. Klobuchar , Ms. Hirono , Mr. Booker , Mr. Schiff , Mr. Murphy , Ms. Warren , Mrs. Gillibrand , Mr. Schatz , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to require federally licensed firearms importers, manufacturers, and dealers to meet certain requirements with respect to securing their firearms inventory, business records, and business premises.\n#### 1. Short title\nThis Act may be cited as the Safety Enhancements for Communities Using Reasonable and Effective Firearm Storage Act or the SECURE Firearm Storage Act .\n#### 2. Security requirements for federally licensed firearms importers, manufacturers, and dealers\n##### (a) In general\nSection 923 of title 18, United States Code, is amended by adding at the end the following:\n(m) Security requirements (1) Relation to provision governing gun shows This subsection shall apply to a licensed importer, licensed manufacturer, or licensed dealer except as provided in subsection (j). (2) Firearm storage (A) In general A person who is a licensed importer, licensed manufacturer, or licensed dealer shall keep and store each firearm in the business inventory of the licensee at the premises covered by the license. (B) Means of storage When the premises covered by the license are not open for business, the licensee shall, with respect to each firearm in the business inventory of the licensee\u2014 (i) secure the firearm with a hardened steel rod 1/4 inch thick through the space between the trigger guard, and the frame or receiver, of the firearm, with\u2014 (I) the steel rod secured by a hardened steel lock that has a shackle; (II) the lock and shackle protected or shielded from the use of a bolt cutter; and (III) the rod anchored to prevent the removal of the firearm from the premises; or (ii) store the firearm in\u2014 (I) a locked fireproof safe; (II) a locked gun cabinet (and if the locked gun cabinet is not steel, each firearm within the cabinet shall be secured with a hardened steel rod 1/4 inch thick, protected or shielded from the use of a bolt cutter and anchored to prevent the removal of the firearm from the premises); or (III) a locked vault. (3) Paper record storage When the premises covered by the license are not open for business, the licensee shall store each paper record of the business inventory and firearm transactions of, and other dispositions of firearms by, the licensee at the premises in a secure location such as a locked fireproof safe or locked vault. (4) Additional security requirements The Attorney General may, by regulation, prescribe such additional security requirements as the Attorney General determines appropriate with respect to the firearms business conducted by a licensed importer, licensed manufacturer, or licensed dealer, such as requirements relating to the use of\u2014 (A) alarm and security camera systems; (B) site hardening; (C) measures to secure any electronic record of the business inventory and firearm transactions of, and other dispositions of firearms by, the licensee; and (D) other measures necessary to reduce the risk of theft at the business premises of a licensee. .\n##### (b) Penalties\nSection 924 of title 18, United States Code, is amended by adding at the end the following:\n(q) Penalties for noncompliance with firearms licensee security requirements (1) In general (A) Penalty With respect to a violation by a licensee of section 923(m) or a regulation issued under that section, the Attorney General, after notice and opportunity for hearing\u2014 (i) in the case of the first violation or related series of violations on the same date, shall subject the licensee to a civil penalty in an amount equal to not less than $1,000 and not more than $10,000; (ii) in the case of the second violation or related series of violations on the same date\u2014 (I) shall suspend the license issued to the licensee under this chapter until the licensee cures the violation; and (II) may subject the licensee to a civil penalty in an amount provided in clause (i); or (iii) in the case of the third violation or related series of violations on the same date\u2014 (I) shall revoke the license issued to the licensee under this chapter; and (II) may subject the licensee to a civil penalty in an amount provided in clause (i). (B) Review An action of the Attorney General under this paragraph may be reviewed only as provided under section 923(f). (2) Administrative remedies The imposition of a civil penalty or suspension or revocation of a license under paragraph (1) shall not preclude any administrative remedy that is otherwise available to the Attorney General. .\n##### (c) Application requirement\nSection 923 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), in the second sentence, by striking be in such form and contain only that and inserting describe how the applicant plans to comply with subsection (m) and shall be in such form and contain only such other ; and\n**(2)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (F), by striking and at the end;\n**(B)**\nin subparagraph (G), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(H) the Attorney General determines that the description in the application of how the applicant plans to comply with subsection (m) would, if implemented, so comply. .\n##### (d) Effective dates\n**(1) Initial firearm storage requirements**\nSection 923(m)(2) of title 18, United States Code, as added by subsection (a), shall take effect on the date that is 1 year after the date of enactment of this Act.\n**(2) Initial paper records storage requirements**\nSection 923(m)(3) of title 18, United States Code, as added by subsection (a), shall take effect on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1097",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SECURE Firearm Storage Act",
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
            "name": "Business records",
            "updateDate": "2025-04-24T15:52:21Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-24T15:52:21Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-04-24T15:52:21Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-04-24T15:52:21Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-24T15:52:21Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-04-24T15:52:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-12T14:19:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s468",
          "measure-number": "468",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s468v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Safety Enhancements for Communities Using Reasonable and Effective Firearm Storage Act or the SECURE Firearm Storage Act</b></p> <p>This bill establishes security requirements for the business premises of a licensed firearms importer, manufacturer, or dealer.</p> <p>Specifically, when the premises are closed for business, an importer, manufacturer, or dealer must secure the firearms inventory and securely store paper business records.</p> <p>A violator is subject to penalties\u2014a civil fine, suspension or revocation of a license, or both a civil fine and suspension or revocation of a license.</p>"
        },
        "title": "SECURE Firearm Storage Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s468.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Safety Enhancements for Communities Using Reasonable and Effective Firearm Storage Act or the SECURE Firearm Storage Act</b></p> <p>This bill establishes security requirements for the business premises of a licensed firearms importer, manufacturer, or dealer.</p> <p>Specifically, when the premises are closed for business, an importer, manufacturer, or dealer must secure the firearms inventory and securely store paper business records.</p> <p>A violator is subject to penalties\u2014a civil fine, suspension or revocation of a license, or both a civil fine and suspension or revocation of a license.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119s468"
    },
    "title": "SECURE Firearm Storage Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Safety Enhancements for Communities Using Reasonable and Effective Firearm Storage Act or the SECURE Firearm Storage Act</b></p> <p>This bill establishes security requirements for the business premises of a licensed firearms importer, manufacturer, or dealer.</p> <p>Specifically, when the premises are closed for business, an importer, manufacturer, or dealer must secure the firearms inventory and securely store paper business records.</p> <p>A violator is subject to penalties\u2014a civil fine, suspension or revocation of a license, or both a civil fine and suspension or revocation of a license.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119s468"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s468is.xml"
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
      "title": "SECURE Firearm Storage Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SECURE Firearm Storage Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safety Enhancements for Communities Using Reasonable and Effective Firearm Storage Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to require federally licensed firearms importers, manufacturers, and dealers to meet certain requirements with respect to securing their firearms inventory, business records, and business premises.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:05Z"
    }
  ]
}
```
