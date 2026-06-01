# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/589
- Title: Providing for the public release of certain documents, records, and communications related to the investigation of Jeffrey Epstein.
- Congress: 119
- Bill type: HRES
- Bill number: 589
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-10-29T08:05:57Z
- Update date including text: 2025-10-29T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-07-17 - IntroReferral: Submitted in House
- 2025-07-17 - IntroReferral: Submitted in House
- 2025-07-21 12:18:13 - Floor: Rules Committee Resolution H. Res. 598 Reported to House. Rule provides for consideration of H. Res. 589. The resolution provides that H.Res. 589 is hereby adopted.
- Latest action: 2025-07-17: Submitted in House

## Actions

- 2025-07-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-07-17 - IntroReferral: Submitted in House
- 2025-07-17 - IntroReferral: Submitted in House
- 2025-07-21 12:18:13 - Floor: Rules Committee Resolution H. Res. 598 Reported to House. Rule provides for consideration of H. Res. 589. The resolution provides that H.Res. 589 is hereby adopted.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/589",
    "number": "589",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000190",
        "district": "5",
        "firstName": "Ralph",
        "fullName": "Rep. Norman, Ralph [R-SC-5]",
        "lastName": "Norman",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Providing for the public release of certain documents, records, and communications related to the investigation of Jeffrey Epstein.",
    "type": "HRES",
    "updateDate": "2025-10-29T08:05:57Z",
    "updateDateIncludingText": "2025-10-29T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1L210",
      "actionDate": "2025-07-21",
      "actionTime": "12:18:13",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Rules Committee Resolution H. Res. 598 Reported to House. Rule provides for consideration of H. Res. 589. The resolution provides that H.Res. 589 is hereby adopted.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-07-17T13:09:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "NC"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "MN"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "IN"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "VA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MO"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "SC"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "SD"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "OK"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NE"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres589ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 589\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Norman (for himself, Ms. Foxx , Mrs. Fischbach , Mr. Roy , Mrs. Houchin , Mr. Langworthy , Mr. Austin Scott of Georgia , Mr. Griffith , and Mr. Jack ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nProviding for the public release of certain documents, records, and communications related to the investigation of Jeffrey Epstein.\n1. Release of documents relating to jeffrey epstein (a) In general Not later than 30 days after the date of enactment of this Resolution, the Attorney General shall, subject to subsection (b), make publicly available in a searchable and downloadable format all credible: (1) documents, records, and communications, including metadata, in the possession of the Department of Justice, including the Federal Bureau of Investigation and United States Attorneys\u2019 Offices, referring or related to the investigation of Jeffrey Epstein and Ghislaine Maxwell. (2) documents, records, and communications, including metadata, between or among Department of Justice employees, including the Federal Bureau of Investigation and United States Attorney\u2019s Offices, referring or relating to the investigation of Jeffrey Epstein and Ghislaine Maxwell. (3) documents, records, and communications, including metadata, referring or relating to United States v. Maxwell, United States v. Jeffrey Epstein, and Farmer v. United States. (4) documents, records, and communications, including metadata, related to Jeffrey Epstein\u2019s detention or death, including any investigation into his death. (b) Prohibited grounds for withholding No record shall be withheld, delayed, or redacted on the basis of any of the following: (1) Embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary. (c) Permitted withholdings (1) The Attorney General may withhold or redact the segregable portions of records that\u2014 (A) contain personally identifiable information of victims of sexual abuse or human trafficking or such victims\u2019 personal and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy, including information that could reasonably be used to unmask or identify such victims of sexual abuse or human trafficking; (B) depicts child pornography, constitutes child sexual abuse or similar materials; (C) would jeopardize an active Federal investigation or ongoing prosecution, provided that such withholding is narrowly tailored; (D) would violate, if disclosed, Rule 6(e) of the Federal Rules of Criminal Procedure by disclosing information that reveals the identities of witnesses or jurors, the substance of testimony before the grand jury, the strategy or direction of the grand jury\u2019s investigation, or the deliberations or questions of jurors, provided that the withholding of information that was coincidentally before the grand jury and can be revealed in such a manner that its disclosure would not elucidate the inner workings of the grand jury is not permitted; (E) depicts or contains images of death, physical abuse, or injury of any person; (F) contain information specifically authorized under criteria established by an Executive order to be kept secret in the interest of national defense or foreign policy and are in fact properly classified pursuant to such Executive order; and (G) are demonstrably false or unauthenticated. (2) All redactions must be accompanied by a written justification published in the Federal Register and submitted to Congress. (3) To the extent that any covered information would otherwise be redacted or withheld as classified information, the Attorney General shall declassify that classified information to the maximum extent possible. (A) If the Attorney General makes a determination that covered information may not be declassified and made available in a manner that protects the national security of the United States, including methods or sources related to national security, the Attorney General shall release an unclassified summary for each of the redacted or withheld classified information. (4) All decisions to classify any covered information after July 1, 2025, shall be published in the Federal Register and submitted to Congress, including the date of classification, the identity of the classifying authority, and an unclassified summary of the justification. 3. Report to congress Within 15 days of completion of the release required under Section 2, the Attorney General shall submit to the House and Senate Committees on the Judiciary a report listing: (1) All categories of records released and withheld. (2) A summary of redactions made, including legal basis. (3) A list of all government officials and politically exposed persons named or referenced in the released materials, with no redactions permitted under subsection (b)(1). .",
      "versionDate": "2025-07-17",
      "versionType": "IH"
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
        "actionDate": "2025-09-03",
        "actionTime": "14:07:30",
        "text": "Pursuant to the provisions of H. Res. 672, H. Res. 598 is laid on the table."
      },
      "number": "598",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "House",
          "type": "Procedurally related"
        }
      },
      "title": "Providing for the adoption of the resolution (H. Res. 589) providing for the public release of certain documents, records, and communications related to the investigation of Jeffrey Epstein.",
      "type": "HRES"
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
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-08-06T13:57:45Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-08-06T13:56:38Z"
          },
          {
            "name": "Freedom of information",
            "updateDate": "2025-08-18T13:43:20Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-18T13:43:10Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-08-06T13:56:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-08-01T14:20:26Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres589ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Providing for the public release of certain documents, records, and communications related to the investigation of Jeffrey Epstein.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for the public release of certain documents, records, and communications related to the investigation of Jeffrey Epstein.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T14:12:42Z"
    }
  ]
}
```
