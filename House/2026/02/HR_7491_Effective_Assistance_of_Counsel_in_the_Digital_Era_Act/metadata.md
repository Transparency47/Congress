# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7491?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7491
- Title: Effective Assistance of Counsel in the Digital Era Act
- Congress: 119
- Bill type: HR
- Bill number: 7491
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-04-03T15:17:25Z
- Update date including text: 2026-04-03T15:17:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7491",
    "number": "7491",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000631",
        "district": "4",
        "firstName": "Madeleine",
        "fullName": "Rep. Dean, Madeleine [D-PA-4]",
        "lastName": "Dean",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Effective Assistance of Counsel in the Digital Era Act",
    "type": "HR",
    "updateDate": "2026-04-03T15:17:25Z",
    "updateDateIncludingText": "2026-04-03T15:17:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:01:25Z",
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
      "bioguideId": "J000294",
      "district": "8",
      "firstName": "Hakeem",
      "fullName": "Rep. Jeffries, Hakeem S. [D-NY-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Jeffries",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7491ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7491\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Ms. Dean of Pennsylvania (for herself, Mr. Jeffries , Ms. Lee of Florida , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo regulate monitoring of electronic communications between an incarcerated person in a Bureau of Prisons facility and that person\u2019s attorney or other legal representative, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Effective Assistance of Counsel in the Digital Era Act .\n#### 2. Electronic communications between an incarcerated person and the person\u2019s attorney\n##### (a) Prohibition on monitoring\nNot later than 180 days after the date of the enactment of this Act, the Attorney General shall create a program or system, or modify any program or system that exists on the date of enactment of this Act, through which an incarcerated person sends or receives an electronic communication, to exclude from monitoring the contents of any privileged electronic communication. In the case that the Attorney General creates a program or system in accordance with this subsection, the Attorney General shall, upon implementing such system, discontinue using any program or system that exists on the date of enactment of this Act through which an incarcerated person sends or receives a privileged electronic communication, except that any program or system that exists on such date may continue to be used for any other electronic communication.\n##### (b) Retention of contents\nA program or system or a modification to a program or system under subsection (a) may allow for retention by the Bureau of Prisons of, and access by an incarcerated person to, the contents of electronic communications, including the contents of privileged electronic communications, of the person until the date on which the person is released from prison.\n##### (c) Attorney-Client privilege\nAttorney-client privilege, and the protections and limitations associated with such privilege (including the crime fraud exception), applies to electronic communications sent or received through the program or system established or modified under subsection (a).\n##### (d) Accessing retained contents\nContents retained under subsection (b) may only be accessed by a person other than the incarcerated person for whom such contents are retained under the following circumstances:\n**(1) Attorney General**\nThe Attorney General may only access retained contents if necessary for the purpose of creating and maintaining the program or system, or any modification to the program or system, through which an incarcerated person sends or receives electronic communications. The Attorney General may not review retained contents that are accessed pursuant to this paragraph.\n**(2) Investigative and law enforcement officers**\n**(A) Warrant**\n**(i) In general**\nRetained contents may only be accessed by an investigative or law enforcement officer pursuant to a warrant issued by a court pursuant to the procedures described in the Federal Rules of Criminal Procedure.\n**(ii) Approval**\nNo application for a warrant may be made to a court without the express approval of a United States Attorney or an Assistant Attorney General.\n**(B) Privileged information**\n**(i) Review**\nBefore retained contents may be accessed pursuant to a warrant obtained under subparagraph (A), such contents shall be reviewed by a United States Attorney to ensure that privileged electronic communications are not accessible.\n**(ii) Barring participation**\nA United States Attorney who reviews retained contents pursuant to clause (i) shall be barred from\u2014\n**(I)**\nparticipating in a legal proceeding in which an individual who sent or received an electronic communication from which such contents are retained under subsection (b) is a defendant; or\n**(II)**\nsharing the retained contents with an attorney who is participating in such a legal proceeding.\n**(3) Motion to suppress**\nIn a case in which retained contents have been accessed in violation of this subsection, a court may suppress evidence obtained or derived from access to such contents upon motion of the defendant.\n##### (e) Definitions\nIn this Act\u2014\n**(1)**\nthe term agent of an attorney or legal representative means any person employed by or contracting with an attorney or legal representative, including law clerks, interns, investigators, paraprofessionals, and administrative staff;\n**(2)**\nthe term contents has the meaning given such term in 2510 of title 18, United States Code;\n**(3)**\nthe term electronic communication has the meaning given such term in section 2510 of title 18, United States Code, and includes the Trust Fund Limited Inmate Computer System;\n**(4)**\nthe term monitoring means accessing the contents of an electronic communication at any time after such communication is sent;\n**(5)**\nthe term incarcerated person means any individual in the custody of the Bureau of Prisons or the United States Marshals Service who has been charged with or convicted of an offense against the United States, including such an individual who is imprisoned in a State institution; and\n**(6)**\nthe term privileged electronic communication means\u2014\n**(A)**\nany electronic communication between an incarcerated person and a potential, current, or former attorney or legal representative of such a person; and\n**(B)**\nany electronic communication between an incarcerated person and the agent of an attorney or legal representative described in subparagraph (A).",
      "versionDate": "2026-02-11",
      "versionType": "Introduced in House"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-20T16:45:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-11",
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
          "measure-id": "id119hr7491",
          "measure-number": "7491",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-11",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7491v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Effective Assistance of Counsel in the Digital Era Act</b></p> <p>This bill prohibits the Department of Justice from monitoring the contents of a privileged electronic communication between an incarcerated person and his or her legal representative.</p>"
        },
        "title": "Effective Assistance of Counsel in the Digital Era Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7491.xml",
    "summary": {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Effective Assistance of Counsel in the Digital Era Act</b></p> <p>This bill prohibits the Department of Justice from monitoring the contents of a privileged electronic communication between an incarcerated person and his or her legal representative.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7491"
    },
    "title": "Effective Assistance of Counsel in the Digital Era Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Effective Assistance of Counsel in the Digital Era Act</b></p> <p>This bill prohibits the Department of Justice from monitoring the contents of a privileged electronic communication between an incarcerated person and his or her legal representative.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7491"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7491ih.xml"
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
      "title": "Effective Assistance of Counsel in the Digital Era Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Effective Assistance of Counsel in the Digital Era Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To regulate monitoring of electronic communications between an incarcerated person in a Bureau of Prisons facility and that person's attorney or other legal representative, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:30Z"
    }
  ]
}
```
