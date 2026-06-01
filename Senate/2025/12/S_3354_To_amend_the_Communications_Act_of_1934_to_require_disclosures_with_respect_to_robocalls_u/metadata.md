# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3354
- Title: QUIET Act
- Congress: 119
- Bill type: S
- Bill number: 3354
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-04-03T14:58:37Z
- Update date including text: 2026-04-03T14:58:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: 
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3354",
    "number": "3354",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "QUIET Act",
    "type": "S",
    "updateDate": "2026-04-03T14:58:37Z",
    "updateDateIncludingText": "2026-04-03T14:58:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
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
      "actionCode": "Intro-S",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:21:35Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3354is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3354\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Curtis (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Communications Act of 1934 to require disclosures with respect to robocalls using artificial intelligence and to provide for enhanced penalties for certain violations involving artificial intelligence voice or text message impersonation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act .\n#### 2. Disclosure required for robocalls using AI\nSection 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ) is amended by adding at the end the following:\n(k) Disclosure required for robocalls using AI (1) In general If a person making a robocall uses artificial intelligence to emulate a human being, such person shall disclose at the beginning of the call or text message the fact that artificial intelligence is being used. (2) Definitions In this subsection: (A) Robocall (i) In general The term robocall means a call made or text message sent\u2014 (I) using equipment, whether hardware, software, or a combination thereof and including an automatic telephone dialing system, that makes a call or sends a text message to\u2014 (aa) stored telephone numbers; or (bb) telephone numbers produced using a random or sequential number generator; or (II) using an artificial or prerecorded voice or an artificially generated message. (ii) Limitation For purposes of clause (i)(I), the term robocall does not include a call made or text message sent using equipment that requires substantial human intervention to make or send the call or text message. (B) Text message (i) In general The term text message means a message consisting of text, images, sounds, or other information that is transmitted to or from a device that is identified as the receiving or transmitting device by means of a 10-digit telephone number, N11 service code, short code telephone number, or email address, or that is transmitted through application-to-person messaging, and includes\u2014 (I) a short message service (commonly referred to as SMS ) message; (II) a multimedia message service (commonly referred to as MMS ) message; and (III) a rich communication service (commonly referred to as RCS ) message. (ii) Limitation The term text message does not include a real-time, two-way voice or video communication. .\n#### 3. Enhanced penalties for violations involving AI voice or text message impersonation\n##### (a) In general\nSection 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ), as amended by section 2 of this Act, is further amended by adding at the end the following:\n(l) Enhanced penalties for violations involving AI voice or text message impersonation In the case of a violation of this section with respect to which the party making the call or sending the text message uses artificial intelligence to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value\u2014 (1) the maximum amount of the forfeiture penalty that may be imposed under subsection (b)(4) or (e)(5)(A) of this section or subsection (b) of section 503 (as the case may be) shall be twice the maximum amount that may be imposed for such violation under such subsection without regard to this subsection; and (2) the maximum amount of the criminal fine that may be imposed under subsection (e)(5)(B) of this section or section 501 (as the case may be) shall be twice the maximum amount that may be imposed for such violation under such subsection or section without regard to this subsection. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to violations occurring after the date of the enactment of this Act.",
      "versionDate": "2025-12-04",
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
        "text": "Sponsor introductory remarks on measure. (CR H519)"
      },
      "number": "1027",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "QUIET Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-07T17:17:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-04",
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
          "measure-id": "id119s3354",
          "measure-number": "3354",
          "measure-type": "s",
          "orig-publish-date": "2025-12-04",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3354v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-12-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act</strong></p><p>This bill establishes a disclosure requirement for robocalls that use artificial intelligence (AI) to emulate a human being and increases forfeiture and fine amounts for certain violations of the Telephone Consumer Protection Act (TCPA). (The TCPA prohibits certain telemarketing calls made without the recipient\u2019s consent and using specified automated technologies.)</p><p>Specifically, any robocall that uses AI to emulate a human being must include a disclosure at the beginning of the message indicating that AI is being used. Under the bill, <em>robocalls</em> are defined as calls made or text messages sent (1) using automatic dialing technology, or (2) using an artificially generated message or an artificial or prerecorded voice. Calls or texts that are made or sent using equipment that requires substantial human intervention are excluded.\u00a0</p><p>Further, the bill doubles the maximum forfeiture penalty and criminal fine that may be imposed for certain violations of the TCPA involving the use of AI to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value. This provision applies to violations that occur after the bill\u2019s enactment.\u00a0</p>"
        },
        "title": "QUIET Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3354.xml",
    "summary": {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act</strong></p><p>This bill establishes a disclosure requirement for robocalls that use artificial intelligence (AI) to emulate a human being and increases forfeiture and fine amounts for certain violations of the Telephone Consumer Protection Act (TCPA). (The TCPA prohibits certain telemarketing calls made without the recipient\u2019s consent and using specified automated technologies.)</p><p>Specifically, any robocall that uses AI to emulate a human being must include a disclosure at the beginning of the message indicating that AI is being used. Under the bill, <em>robocalls</em> are defined as calls made or text messages sent (1) using automatic dialing technology, or (2) using an artificially generated message or an artificial or prerecorded voice. Calls or texts that are made or sent using equipment that requires substantial human intervention are excluded.\u00a0</p><p>Further, the bill doubles the maximum forfeiture penalty and criminal fine that may be imposed for certain violations of the TCPA involving the use of AI to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value. This provision applies to violations that occur after the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s3354"
    },
    "title": "QUIET Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act</strong></p><p>This bill establishes a disclosure requirement for robocalls that use artificial intelligence (AI) to emulate a human being and increases forfeiture and fine amounts for certain violations of the Telephone Consumer Protection Act (TCPA). (The TCPA prohibits certain telemarketing calls made without the recipient\u2019s consent and using specified automated technologies.)</p><p>Specifically, any robocall that uses AI to emulate a human being must include a disclosure at the beginning of the message indicating that AI is being used. Under the bill, <em>robocalls</em> are defined as calls made or text messages sent (1) using automatic dialing technology, or (2) using an artificially generated message or an artificial or prerecorded voice. Calls or texts that are made or sent using equipment that requires substantial human intervention are excluded.\u00a0</p><p>Further, the bill doubles the maximum forfeiture penalty and criminal fine that may be imposed for certain violations of the TCPA involving the use of AI to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value. This provision applies to violations that occur after the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s3354"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3354is.xml"
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
      "title": "QUIET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "QUIET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Quashing Unwanted and Interruptive Electronic Telecommunications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Communications Act of 1934 to require disclosures with respect to robocalls using artificial intelligence and to provide for enhanced penalties for certain violations involving artificial intelligence voice or text message impersonation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:24Z"
    }
  ]
}
```
