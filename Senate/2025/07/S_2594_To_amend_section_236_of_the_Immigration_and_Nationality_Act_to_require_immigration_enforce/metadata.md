# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2594?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2594
- Title: IEIS Act
- Congress: 119
- Bill type: S
- Bill number: 2594
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-12-02T12:03:45Z
- Update date including text: 2025-12-02T12:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2594",
    "number": "2594",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "IEIS Act",
    "type": "S",
    "updateDate": "2025-12-02T12:03:45Z",
    "updateDateIncludingText": "2025-12-02T12:03:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T18:17:29Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "VA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-31",
      "state": "ME"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CO"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CO"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "DE"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2594is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2594\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Warner (for himself, Mr. Kaine , Mr. King , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 236 of the Immigration and Nationality Act to require immigration enforcement officers of the Department of Homeland Security to display visible identification during enforcement actions and provide privacy enhancing services.\n#### 1. Short titles\nThis Act may be cited as the Immigration Enforcement Identification Safety Act of 2025 or the IEIS Act .\n#### 2. Definitions\nIn this Act:\n##### (a) Agency\nThe term agency means an Executive agency (as defined in section 105 of title 5, United States Code).\n##### (b) Covered employee\nThe term covered employee means\u2014\n**(1)**\na covered immigration officer (as defined in section 236(g)(1)(A) of the Immigration and Nationality Act, as amended by section 2), whose official duties put the covered employee at greater risk of being the target of a threat, intimidation, harassment, stalking, or a similar action;\n**(2)**\na spouse, child, or parent of an employee described in subparagraph (A); and\n**(3)**\nany other familial relative of such employee who has the same permanent residence as such employee.\n##### (c) Privacy-Enhancing services\nThe term privacy-enhancing services means any software or hardware solution, technical process, technique, or other technological means of mitigating privacy risks arising from data processing, including by eliminating, reducing, or suppressing personal information, including restricted personal information (as defined in section 119(b)(1) of title 18, United States Code).\n#### 3. Identification requirement for immigration enforcement personnel\nSection 236 of the Immigration and Nationality Act ( 8 U.S.C. 1226 ) is amended by adding at the end the following:\n(g) Identification requirement for immigration enforcement personnel (1) Definitions In this subsection: (A) Covered immigration officer The term covered immigration officer means\u2014 (i) any officer, agent, or employee of U.S. Customs and Border Protection; (ii) any officer, agent, or employee of U.S. Immigration and Customs Enforcement; and (iii) any officer, agent, or individual authorized, deputized, or designated under Federal law, regulation, or agreement to perform immigration enforcement functions, including pursuant to section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ) or any other delegation or agreement with the Department of Homeland Security. (B) Immigration enforcement function The term immigration enforcement function \u2014 (i) means any activity that involves the direct exercise of Federal immigration enforcement through public-facing actions, including a patrol, stop, arrest, search, interview to determine immigration status, raid, checkpoint, or the service of a judicial or administrative warrant; and (ii) does not include any covert, nonpublic operation. (2) In general Except as provided in paragraph (3), any covered immigration officer who is conducting an immigration enforcement function and any Federal or non-Federal law enforcement officer who is providing direct support to such immigration enforcement function shall visibly display\u2014 (A) such covered immigration officer's last name and another individual identifier that is unique to such individual; (B) the name of the Federal law enforcement entity or other organization employing such covered immigration officer; and (C) the face of such covered immigration officer. (3) Exception The requirement under paragraph (2) shall not apply to individuals referred to in such paragraph who\u2014 (A) are engaged in investigative activity involving the use of an assumed name or cover identity; (B) are engaged in planned tactical operations (such as high-risk situations, responding to hostage incidents, terrorism response, narcotics raids, hazardous surveillance, sniper incidents, armed suicidal persons, barricaded suspects, high-risk felony warrant service, fugitives refusing to surrender, and active shooter incidents) by specifically trained law enforcement personnel to a high-risk situation that requires the application of specialized lifesaving tools, tactics, and capabilities which exceed those immediately available to the officer or agent of the Department of Homeland Security who is conducting an immigration enforcement function and any Federal or non-Federal law enforcement officer who is providing direct support to such immigration enforcement function in the regular performance of the officer's or agent's official duties; or (C) are engaged in a law enforcement function that necessitate the use of face coverings, as required under section 1960.10(b) of title 29, Code of Federal Regulations. .\n#### 4. Reimbursements relating to internet data privacy services\n##### (a) In general\nNotwithstanding any other provision of law, amounts appropriated by any Act for fiscal year 2026, or for any fiscal year thereafter, for salaries and expenses of an agency may be used by such agency to reimburse a covered employee employed by that agency for not more than 100 percent of the costs incurred by the covered employee for privacy-enhancing services.\n##### (b) Documentation\nAny reimbursement to a covered employee authorized under subsection (a) shall be contingent upon the submission by the covered employee of such information or documentation as the agency employing the covered employee may reasonably require.\n#### 5. Rules of construction\nNothing in this Act may be construed to prohibit, restrain, or limit\u2014\n**(1)**\nthe lawful investigation or reporting by the press of any unlawful activity or misconduct alleged to have been committed by a covered employee;\n**(2)**\nthe lawful disclosure of information relating to a covered employee or the immediate family of a covered employee regarding matters of public concern; or\n**(3)**\ninformation that the covered employee or the employer of the covered employee voluntarily publishes on the internet after the date of the enactment of this Act.",
      "versionDate": "2025-07-31",
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
        "name": "Immigration",
        "updateDate": "2025-09-18T19:44:07Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2594is.xml"
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
      "title": "IEIS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "IEIS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Immigration Enforcement Identification Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 236 of the Immigration and Nationality Act to require immigration enforcement officers of the Department of Homeland Security to display visible identification during enforcement actions and provide privacy enhancing services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:24Z"
    }
  ]
}
```
