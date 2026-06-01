# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/463?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/463
- Title: Protect Our Letter Carriers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 463
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-05-19T11:03:43Z
- Update date including text: 2026-05-19T11:03:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/463",
    "number": "463",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Protect Our Letter Carriers Act of 2025",
    "type": "S",
    "updateDate": "2026-05-19T11:03:43Z",
    "updateDateIncludingText": "2026-05-19T11:03:43Z"
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
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
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
        "item": [
          {
            "date": "2025-02-06T19:12:45Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T19:12:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NH"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NM"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MD"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "DE"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "DE"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CO"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s463is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 463\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mrs. Gillibrand (for herself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo facilitate the implementation of security measures undertaken by the United States Postal Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Our Letter Carriers Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of the Congress that\u2014\n**(1)**\nUnited States Postal Service letter carriers must be protected from acts of violence; and\n**(2)**\nthe Attorney General should vigorously prosecute any case of assault against a postal employee.\n#### 3. Funds to upgrade collection boxes\nThere is authorized to be appropriated $1,400,000,000 for each of fiscal years 2025 through 2029 to the United States Postal Service to carry out, as determined by the United States Postal Service\u2014\n**(1)**\nthe installation of high security collection boxes; and\n**(2)**\nthe replacement of older versions of the universal mailbox key, also known as the arrow key, with electronic versions.\n#### 4. Coordination of prosecution of offenses against the United States Postal Service\n##### (a) In general\nSection 542 of title 28, United States Code, is amended by adding at the end the following:\n(c) The Attorney General shall, in consultation with the United States attorney for the district, appoint in each judicial district an assistant United States attorney with principal responsibility in the district to coordinate and supervise the investigation and prosecution of alleged offenses committed\u2014 (1) in violation of chapter 83 of title 18; (2) in violation of sections 2115, 2116, or 2117 of title 18; or (3) against a carrier or person entrusted with the mail and having custody thereof, in violation of section 111 of title 18. .\n##### (b) Deadline for compliance\nThe Attorney General shall comply with section 542(c) of title 28, United States Code, as added by this Act, not later than 1 year after the date of the enactment of this Act.\n#### 5. Sentencing guidelines with respect to robbery against a postal employee\nNot later than May 1 following the first year that begins after the date of enactment of this Act, the United States Sentencing Commission shall amend the sentencing guidelines and policy statements promulgated under section 994 of title 28, United States Code, to provide that the assault or robbery of a postal employee, including conduct committed during the immediate flight after the commission of such an assault or robbery if the conduct creates a substantial risk of serious bodily injury, shall be treated in the same manner as the assault of a law enforcement officer.",
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
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1065",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Our Letter Carriers Act of 2025",
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
            "name": "Administrative remedies",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Customs enforcement",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "Property rights",
            "updateDate": "2025-03-27T14:52:53Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-27T14:52:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-12T17:29:11Z"
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
          "measure-id": "id119s463",
          "measure-number": "463",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s463v00",
            "update-date": "2025-05-24"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect Our Letter Carriers Act of 2025</strong><br/><br/>This bill requires or authorizes certain actions related to the U.S. Postal Service (USPS).<br/><br/>The bill requires the Department of Justice to appoint an assistant U.S. attorney in each judicial district to coordinate and supervise the investigation and prosecution of various crimes related to postal services (for example, assault on a postal service employee, breaking into a post office, or obstruction of mails). <br/><br/>The bill also requires the U.S. Sentencing Commission to amend sentencing guidelines to provide that the assault or robbery of a postal employee shall be treated the same as the assault of a law enforcement officer.</p><p>Additionally, the bill authorizes appropriations for the USPS to install high security collection boxes and replace older versions of the universal mailbox key with electronic versions.</p>"
        },
        "title": "Protect Our Letter Carriers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s463.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Our Letter Carriers Act of 2025</strong><br/><br/>This bill requires or authorizes certain actions related to the U.S. Postal Service (USPS).<br/><br/>The bill requires the Department of Justice to appoint an assistant U.S. attorney in each judicial district to coordinate and supervise the investigation and prosecution of various crimes related to postal services (for example, assault on a postal service employee, breaking into a post office, or obstruction of mails). <br/><br/>The bill also requires the U.S. Sentencing Commission to amend sentencing guidelines to provide that the assault or robbery of a postal employee shall be treated the same as the assault of a law enforcement officer.</p><p>Additionally, the bill authorizes appropriations for the USPS to install high security collection boxes and replace older versions of the universal mailbox key with electronic versions.</p>",
      "updateDate": "2025-05-24",
      "versionCode": "id119s463"
    },
    "title": "Protect Our Letter Carriers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Our Letter Carriers Act of 2025</strong><br/><br/>This bill requires or authorizes certain actions related to the U.S. Postal Service (USPS).<br/><br/>The bill requires the Department of Justice to appoint an assistant U.S. attorney in each judicial district to coordinate and supervise the investigation and prosecution of various crimes related to postal services (for example, assault on a postal service employee, breaking into a post office, or obstruction of mails). <br/><br/>The bill also requires the U.S. Sentencing Commission to amend sentencing guidelines to provide that the assault or robbery of a postal employee shall be treated the same as the assault of a law enforcement officer.</p><p>Additionally, the bill authorizes appropriations for the USPS to install high security collection boxes and replace older versions of the universal mailbox key with electronic versions.</p>",
      "updateDate": "2025-05-24",
      "versionCode": "id119s463"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s463is.xml"
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
      "title": "Protect Our Letter Carriers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Our Letter Carriers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to facilitate the implementation of security measures undertaken by the United States Postal Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:54Z"
    }
  ]
}
```
