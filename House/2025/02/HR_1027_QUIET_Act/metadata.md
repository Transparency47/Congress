# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1027
- Title: QUIET Act
- Congress: 119
- Bill type: HR
- Bill number: 1027
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2026-05-14T08:08:48Z
- Update date including text: 2026-05-14T08:08:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H519)
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-06 - IntroReferral: Sponsor introductory remarks on measure. (CR H519)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1027",
    "number": "1027",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001225",
        "district": "17",
        "firstName": "Eric",
        "fullName": "Rep. Sorensen, Eric [D-IL-17]",
        "lastName": "Sorensen",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "QUIET Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:48Z",
    "updateDateIncludingText": "2026-05-14T08:08:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H519)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:00:20Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "AZ"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "PA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "DC"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "AZ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "VA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "DE"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NM"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "PR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "OR"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "PA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "AZ"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1027ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1027\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Sorensen (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to require disclosures with respect to robocalls using artificial intelligence and to provide for enhanced penalties for certain violations involving artificial intelligence voice or text message impersonation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act .\n#### 2. Disclosure required for robocalls using AI\nSection 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ) is amended by adding at the end the following:\n(k) Disclosure required for robocalls using AI (1) In general If a person making a robocall uses artificial intelligence to emulate a human being, such person shall disclose at the beginning of the call or text message the fact that artificial intelligence is being used. (2) Definitions In this subsection: (A) Robocall (i) In general The term robocall means a call made or text message sent\u2014 (I) using equipment, whether hardware, software, or a combination thereof and including an automatic telephone dialing system, that makes a call or sends a text message to\u2014 (aa) stored telephone numbers; or (bb) telephone numbers produced using a random or sequential number generator; or (II) using an artificial or prerecorded voice or an artificially generated message. (ii) Limitation For purposes of clause (i)(I), the term robocall does not include a call made or text message sent using equipment that requires substantial human intervention to make or send the call or text message. (B) Text message (i) In general The term text message means a message consisting of text, images, sounds, or other information that is transmitted to or from a device that is identified as the receiving or transmitting device by means of a 10-digit telephone number, N11 service code, short code telephone number, or email address, or that is transmitted through application-to-person messaging, and includes\u2014 (I) a short message service (commonly referred to as SMS ) message; (II) a multimedia message service (commonly referred to as MMS ) message; and (III) a rich communication service (commonly referred to as RCS ) message. (ii) Limitation The term text message does not include a real-time, two-way voice or video communication. .\n#### 3. Enhanced penalties for violations involving AI voice or text message impersonation\n##### (a) In general\nSection 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ), as amended by the preceding provisions of this Act, is further amended by adding at the end the following:\n(l) Enhanced penalties for violations involving AI voice or text message impersonation In the case of a violation of this section with respect to which the party making the call or sending the text message uses artificial intelligence to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value\u2014 (1) the maximum amount of the forfeiture penalty that may be imposed under subsection (b)(4) or (e)(5)(A) of this section or subsection (b) of section 503 (as the case may be) shall be twice the maximum amount that may be imposed for such violation under such subsection without regard to this subsection; and (2) the maximum amount of the criminal fine that may be imposed under subsection (e)(5)(B) of this section or section 501 (as the case may be) shall be twice the maximum amount that may be imposed for such violation under such subsection or section without regard to this subsection. .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to violations occurring after the date of the enactment of this Act.",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3354",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "QUIET Act",
      "type": "S"
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
        "updateDate": "2025-03-07T16:50:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hr1027",
          "measure-number": "1027",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-04-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1027v00",
            "update-date": "2025-04-11"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act</strong></p><p>This bill establishes a disclosure requirement for robocalls that use artificial intelligence (AI) to emulate a human being and increases forfeiture and fine amounts for certain violations of the Telephone Consumer Protection Act (TCPA). (The TCPA prohibits certain telemarketing calls made without the recipient\u2019s consent and using specified automated technologies.)</p><p>Specifically, any robocall that uses AI to emulate a human being must include a disclosure at the beginning of the message indicating that AI is being used. Under the bill, <em>robocalls</em> are defined as calls made or text messages sent (1) using automatic dialing technology, or (2) using an artificially generated message or an artificial or prerecorded voice. Calls or texts that are made or sent using equipment that requires substantial human intervention are excluded.\u00a0</p><p>Further, the bill doubles the maximum forfeiture penalty and criminal fine that may be imposed for certain violations of the TCPA involving the use of AI to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value. This provision applies to violations that occur after the bill\u2019s enactment.\u00a0</p>"
        },
        "title": "QUIET Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1027.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act</strong></p><p>This bill establishes a disclosure requirement for robocalls that use artificial intelligence (AI) to emulate a human being and increases forfeiture and fine amounts for certain violations of the Telephone Consumer Protection Act (TCPA). (The TCPA prohibits certain telemarketing calls made without the recipient\u2019s consent and using specified automated technologies.)</p><p>Specifically, any robocall that uses AI to emulate a human being must include a disclosure at the beginning of the message indicating that AI is being used. Under the bill, <em>robocalls</em> are defined as calls made or text messages sent (1) using automatic dialing technology, or (2) using an artificially generated message or an artificial or prerecorded voice. Calls or texts that are made or sent using equipment that requires substantial human intervention are excluded.\u00a0</p><p>Further, the bill doubles the maximum forfeiture penalty and criminal fine that may be imposed for certain violations of the TCPA involving the use of AI to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value. This provision applies to violations that occur after the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2025-04-11",
      "versionCode": "id119hr1027"
    },
    "title": "QUIET Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Quashing Unwanted and Interruptive Electronic Telecommunications Act or the QUIET Act</strong></p><p>This bill establishes a disclosure requirement for robocalls that use artificial intelligence (AI) to emulate a human being and increases forfeiture and fine amounts for certain violations of the Telephone Consumer Protection Act (TCPA). (The TCPA prohibits certain telemarketing calls made without the recipient\u2019s consent and using specified automated technologies.)</p><p>Specifically, any robocall that uses AI to emulate a human being must include a disclosure at the beginning of the message indicating that AI is being used. Under the bill, <em>robocalls</em> are defined as calls made or text messages sent (1) using automatic dialing technology, or (2) using an artificially generated message or an artificial or prerecorded voice. Calls or texts that are made or sent using equipment that requires substantial human intervention are excluded.\u00a0</p><p>Further, the bill doubles the maximum forfeiture penalty and criminal fine that may be imposed for certain violations of the TCPA involving the use of AI to impersonate an individual or entity with the intent to defraud, cause harm, or wrongfully obtain anything of value. This provision applies to violations that occur after the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2025-04-11",
      "versionCode": "id119hr1027"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1027ih.xml"
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
      "title": "QUIET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "QUIET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quashing Unwanted and Interruptive Electronic Telecommunications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Communications Act of 1934 to require disclosures with respect to robocalls using artificial intelligence and to provide for enhanced penalties for certain violations involving artificial intelligence voice or text message impersonation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T13:18:23Z"
    }
  ]
}
```
