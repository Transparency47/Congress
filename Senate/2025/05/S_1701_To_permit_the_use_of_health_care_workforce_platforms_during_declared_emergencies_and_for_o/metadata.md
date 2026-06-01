# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1701?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1701
- Title: STORM Act
- Congress: 119
- Bill type: S
- Bill number: 1701
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-01-07T23:23:46Z
- Update date including text: 2026-01-07T23:23:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1701",
    "number": "1701",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "STORM Act",
    "type": "S",
    "updateDate": "2026-01-07T23:23:46Z",
    "updateDateIncludingText": "2026-01-07T23:23:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T19:29:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1701is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1701\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Budd introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo permit the use of health care workforce platforms during declared emergencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategic Teams for Organized Response Mobilization Act or the STORM Act .\n#### 2. Use of health care workforce platforms during state of emergency\nTitle V of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 et seq. ) is amended by adding at the end the following:\n504. Health care workforce platforms (a) Definitions In this section: (1) Emergency The term emergency means an emergency declared under section 501. (2) Health care workforce platform The term health care workforce platform means a private entity technology platform that\u2014 (A) partners with credentialed independent contractor health care workers; (B) has the capability to facilitate health care workforce surge capacity during an emergency; and (C) is self-sustaining during times other than those in which an emergency is declared. (3) Independent contractor health care worker The term independent contractor health care worker means a health care professional who\u2014 (A) holds a valid license to practice as a health care professional in not less than 1 State; (B) provides health care services on a contractual basis, rather than as an employee of a health care facility or organization; (C) is credentialed and verified by a health care workforce platform; and (D) is engaged to respond to health care needs during an emergency. (b) Public-Private partnership (1) Certification The President may certify health care workforce platforms as eligible to enter into an agreement under paragraph (2). (2) Voluntary agreements (A) In general The President may enter into an agreement with a health care workforce platform certified under paragraph (1) under which the President may use the health care workforce platform for the duration of any emergency declared during the term of the agreement. (B) Term The duration of the term of an agreement entered into under subparagraph (A) shall be not less than 1 year. (c) Facilitation of State licensure waivers (1) In general During any emergency, the President may coordinate with States to facilitate a waiver of licensure requirements of the State for out-of-state independent contractor health care workers responding to an emergency through a health care workforce platform with which the President has entered into an agreement under subsection (b)(2) if\u2014 (A) the services of the independent contractor health care worker are being used by the President or the State or a local government affected by the emergency for the purpose of responding to the emergency; and (B) the independent contractor health care worker holds a valid license to practice as a health care worker in not less than 1 State. (2) Procedures and criteria The President shall establish model procedures and criteria for the waiver of State licensure requirements under paragraph (1) that a State affected by an emergency may adopt at the time of the emergency that\u2014 (A) include requirements that independent contractor health care workers demonstrate qualifications and undergo background checks; (B) prioritize the expedited deployment of qualified independent contractor health care workers to areas affected by an emergency; and (C) may rely on vetting of independent contractor health care workers by a health care workforce platform with which the President has entered into an agreement under subsection (b)(2). (3) Coordination with State authorities In carrying out this subsection, the President shall\u2014 (A) coordinate with relevant State authorities to ensure the efficient implementation of licensure waivers or temporary licenses; and (B) consider State-specific regulations and requirements. (d) Reporting requirements Not later than 1 year after the date of enactment of the Strategic Teams for Organized Response Mobilization Act , and annually thereafter, the President shall submit to Congress a report on the use of State licensure waivers during emergencies under this section, including\u2014 (1) information on the number of independent contractor health care workers for whom a State waives a licensure requirement under subsection (c)(1) to facilitate deployment during an emergency; (2) the duration of the deployment of independent contractor health care workers described in paragraph (1); and (3) any challenges encountered in the process of carrying out subsection (c)(1). (e) Liability protections (1) In general Subject to paragraph (2), an independent contractor health care worker or health care workforce platform that engages in activities authorized under this title and complies with or reasonably attempt to comply with this title shall not be liable for any injury or damage sustained to a person or property as a result of such activities. (2) Exception Paragraph (1) shall not apply in a case of willful misconduct, gross negligence, or bad faith. (3) Federal Tort Claims Act Any private entity, including an independent contractor health care worker and a health care workforce platform, that enters into a contract or agreement with the Federal Government or acts at the direction of a Federal agency to respond to an emergency during an emergency the primary responsibility for the response to which the President determines rests with the United States under section 501(b), shall be deemed an employee of the government for purposes of chapter 171 of title 28, United States Code, with respect to claims arising from acts or omissions within the scope of such contract or agreement. (4) Applicability This subsection shall apply only to activities\u2014 (A) conducted in response to an emergency the primary responsibility for the response to which the President determines rests with the United States under section 501(b); and (B) that are within the scope of the duties authorized by this Act. (5) Regulations The President shall issue such regulations as are necessary to implement this section, including regulations to determine the applicability of chapter 171 of title 28, United States Code, to independent contractor health care workers and health care workforce platforms under this section. .",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-12-09",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "6539",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STORM Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-06-09T14:53:13Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1701is.xml"
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
      "title": "STORM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STORM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strategic Teams for Organized Response Mobilization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit the use of health care workforce platforms during declared emergencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:36Z"
    }
  ]
}
```
