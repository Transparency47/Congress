# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3850?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3850
- Title: Effective Assistance of Counsel in the Digital Era Act
- Congress: 119
- Bill type: S
- Bill number: 3850
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3850",
    "number": "3850",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Effective Assistance of Counsel in the Digital Era Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T22:18:33Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "WY"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "KY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3850is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3850\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Wyden (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo regulate monitoring of electronic communications between an incarcerated person in a Bureau of Prisons facility and that person\u2019s attorney or other legal representative, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Effective Assistance of Counsel in the Digital Era Act .\n#### 2. Electronic communications between an incarcerated person and the person\u2019s attorney\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term agent of an attorney or legal representative means any person employed by or contracting with an attorney or legal representative, including law clerks, interns, investigators, paraprofessionals, and administrative staff;\n**(2)**\nthe term contents has the meaning given such term in section 2510 of title 18, United States Code;\n**(3)**\nthe term electronic communication \u2014\n**(A)**\nhas the meaning given such term in section 2510 of title 18, United States Code; and\n**(B)**\nincludes the Trust Fund Limited Inmate Computer System;\n**(4)**\nthe term incarcerated person means any individual in the custody of the Bureau of Prisons or the United States Marshals Service who has been charged with or convicted of an offense against the United States, including such an individual who is imprisoned in a State institution;\n**(5)**\nthe term monitoring means accessing the contents of an electronic communication at the time that, or anytime after, such communication is sent; and\n**(6)**\nthe term privileged electronic communication means\u2014\n**(A)**\nan electronic communication between an incarcerated person and a potential, current, or former attorney or legal representative of the incarcerated person that falls within the legally recognized scope of attorney-client privilege and is subject to the limitations or exceptions associated with such privilege; and\n**(B)**\nan electronic communication between an incarcerated person and the agent of an attorney or legal representative described in subparagraph (A).\n##### (b) Prohibition on monitoring\nNot later than 2 years after the date of enactment of this Act, the Attorney General shall issue a report regarding, establish guidelines for, and create a program or system, or modify a program or system that exists on the date of enactment of this Act, through which an incarcerated person may send or receive an electronic communication that excludes from monitoring the contents of any privileged electronic communication.\n##### (c) Features of program or system\nThe program or system created or modified under subsection (b) shall comply with the following:\n**(1) Retention of contents**\nThe Bureau of Prisons may retain, and provide access by an incarcerated person to, the contents of electronic communications, including the contents of privileged electronic communications, of the incarcerated person until the date on which the incarcerated person is released from the custody of the Bureau of Prisons or the United States Marshals Service.\n**(2) Attorney-client privilege**\nAttorney-client privilege, and the protections and limitations associated with such privilege (including the crime fraud exception), shall apply to electronic communications sent or received through the program or system.\n##### (d) Accessing retained communications\n**(1) In general**\nPrivileged electronic communications retained under subsection (c)(1) may only be accessed by or provided to a person other than the incarcerated person for whom such privileged electronic communications are retained in accordance with paragraphs (2) and (3) of this subsection.\n**(2) Attorney general**\nThe Attorney General, or a designee, may only access such privileged electronic communications if necessary for the purpose of creating and maintaining the program or system created or modified under subsection (b), or any modification to the program or system. The Attorney General may not review the contents of privileged electronic communications pursuant to this paragraph.\n**(3) Investigative and law enforcement officers**\n**(A) Warrant**\n**(i) In general**\nSuch privileged electronic communications may only be accessed and the contents of such privileged electronic communications may only be reviewed by an investigative or law enforcement officer pursuant to a warrant issued by a court pursuant to the procedures described in the Federal Rules of Criminal Procedure.\n**(ii) Waiver**\nAn incarcerated person may waive the requirement to obtain a warrant under clause (i).\n**(iii) Approval**\nNo application for such a warrant may be made to a court without the express approval of a United States attorney, an Assistant Attorney General, or a designee thereof.\n**(B) Privileged information**\nThe Attorney General shall establish procedures concerning the review of privileged electronic communications under subparagraph (A), which shall include the following:\n**(i) Review**\nBefore the contents of such privileged electronic communications may be reviewed by an investigative or law enforcement officer pursuant to a warrant described in subparagraph (A), the privileged electronic communications shall be reviewed by a United States attorney, an Assistant Attorney General, or a designee to determine if a limitation or exception to the attorney-client privilege applies to any of the privileged electronic communications.\n**(ii) Barring participation**\nA United States attorney, an Assistant Attorney General, or a designee who reviews privileged electronic communications pursuant to clause (i) shall be barred from\u2014\n**(I)**\nparticipating in a legal proceeding in which an individual who sent or received such a privileged electronic communication is a defendant; or\n**(II)**\nsharing with an attorney who is participating in such a legal proceeding such a privileged electronic communication.\n**(4) Motion to suppress**\nUpon motion of a defendant, a court may suppress evidence obtained or derived from accessing privileged electronic communications or reviewing the contents of privileged electronic communications in violation of this subsection.\n##### (e) Notice until program or system is operational\nThe Attorney General shall provide written notice to each individual who is an incarcerated person at any time during the period beginning on the date of enactment of this Act and ending on the date on which the program or system created or modified under subsection (b) is operational that the privileged electronic communications of the individual are subject to monitoring.\n##### (f) Rules of construction\n**(1) Inapplicability to non-privileged electronic communications**\nNothing in this section shall be construed to limit the ability of investigative or law enforcement officers to monitor, record, access, review, or retain nonprivileged electronic communications of an incarcerated person.\n**(2) Verification of agent of an attorney or legal representative**\nNothing in this section shall limit the authority of the Bureau of Prisons to establish policies that require a potential, current, or former attorney or legal representative to verify their identity, employment status, or licensure to practice law prior to being granted authorization to receive or send electronic communications from or to an incarcerated person.",
      "versionDate": "2026-02-11",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-02T17:14:35Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3850is.xml"
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
      "title": "Effective Assistance of Counsel in the Digital Era Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Effective Assistance of Counsel in the Digital Era Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to regulate monitoring of electronic communications between an incarcerated person in a Bureau of Prisons facility and that person's attorney or other legal representative, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:03:25Z"
    }
  ]
}
```
