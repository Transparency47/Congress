# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1595?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1595
- Title: Improving Police CARE Act
- Congress: 119
- Bill type: S
- Bill number: 1595
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2026-04-20T19:41:03Z
- Update date including text: 2026-04-20T19:41:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 84.
- 2025-07-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S4796; text: CR S4797)
- 2025-07-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-08-01 - Floor: Message on Senate action sent to the House.
- 2025-08-01 10:02:04 - Floor: Received in the House.
- 2025-08-01 10:02:14 - Floor: Held at the desk.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 84.
- 2025-07-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S4796; text: CR S4797)
- 2025-07-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-08-01 - Floor: Message on Senate action sent to the House.
- 2025-08-01 10:02:04 - Floor: Received in the House.
- 2025-08-01 10:02:14 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1595",
    "number": "1595",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Improving Police CARE Act",
    "type": "S",
    "updateDate": "2026-04-20T19:41:03Z",
    "updateDateIncludingText": "2026-04-20T19:41:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-08-01",
      "actionTime": "10:02:14",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-08-01",
      "actionTime": "10:02:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S4796; text: CR S4797)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 84.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
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
            "date": "2025-05-20T20:25:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-05T22:33:02Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "RI"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "DE"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "SD"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "IL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1595is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1595\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Cornyn (for himself, Mr. Whitehouse , Mr. Tillis , Mr. Coons , Mr. Rounds , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish standards for trauma kits purchased using funds provided under the Edward Byrne Memorial Justice Assistance Grant Program.\n#### 1. Short title\nThis Act may be cited as the Improving Police Critical Aid for Responding to Emergencies Act or the Improving Police CARE Act .\n#### 2. Trauma kit standards\nSection 521 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10202 ) is amended by adding at the end the following:\n(d) Trauma kits (1) Definition In this subsection, the term trauma kit means a first aid response kit, which includes a bleeding control kit that can be used for controlling a life-threatening hemorrhage. (2) Requirement for trauma kits (A) In general Notwithstanding any other provision of law, a grantee may only purchase a trauma kit using funds made available under this part if the trauma kit meets the performance standards established by the Director of the Bureau of Justice Assistance under paragraph (3)(A). (B) Authority to separately acquire Nothing in subparagraph (A) shall prohibit a grantee from separately acquiring the components of a trauma kit and assembling complete trauma kits that meet the performance standards. (3) Performance standards and optional agency best practices Not later than 180 days after the date of enactment of this subsection, the Director of the Bureau of Justice Assistance, in consultation with organizations representing trauma surgeons, emergency medical response professionals, emergency physicians, other medical professionals, relevant law enforcement agencies of States and units of local government, professional law enforcement organizations, local law enforcement labor or representative organizations, and law enforcement trade associations, shall\u2014 (A) develop and publish performance standards for trauma kits that are eligible for purchase using funds made available under this part that, at a minimum, require the components described in paragraph (4) to be included in a trauma kit; and (B) develop and publish optional best practices for law enforcement agencies regarding\u2014 (i) training law enforcement officers in the use of trauma kits; (ii) the deployment and maintenance of trauma kits in law enforcement vehicles; and (iii) the deployment, location, and maintenance of trauma kits in law enforcement agency or other government facilities. (4) Components The components of a trauma kit described in this paragraph are\u2014 (A) a tourniquet recommended by the Committee on Tactical Combat Casualty Care; (B) a bleeding control bandage; (C) a pair of nonlatex protective gloves and a pen-type marker; (D) a pair of blunt-ended scissors; (E) instructional documents developed\u2014 (i) under the Stop the Bleed national awareness campaign of the Department of Homeland Security, or any successor thereto; (ii) by the American College of Surgeons Committee on Trauma; (iii) by the American Red Cross; or (iv) by any partner of the Department of Defense; (F) a bag or other container adequately designed to hold the contents of the kit; and (G) any additional trauma kit supplies that\u2014 (i) are approved by a State, local, or Tribal law enforcement agency or first responders; (ii) can adequately treat a traumatic injury; and (iii) can be stored in a readily available kit. .",
      "versionDate": "2025-05-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1595rs.xml",
      "text": "II\nCalendar No. 84\n119th CONGRESS\n1st Session\nS. 1595\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Cornyn (for himself, Mr. Whitehouse , Mr. Tillis , Mr. Coons , Mr. Rounds , Mr. Durbin , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , without amendment\nA BILL\nTo establish standards for trauma kits purchased using funds provided under the Edward Byrne Memorial Justice Assistance Grant Program.\n#### 1. Short title\nThis Act may be cited as the Improving Police Critical Aid for Responding to Emergencies Act or the Improving Police CARE Act .\n#### 2. Trauma kit standards\nSection 521 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10202 ) is amended by adding at the end the following:\n(d) Trauma kits (1) Definition In this subsection, the term trauma kit means a first aid response kit, which includes a bleeding control kit that can be used for controlling a life-threatening hemorrhage. (2) Requirement for trauma kits (A) In general Notwithstanding any other provision of law, a grantee may only purchase a trauma kit using funds made available under this part if the trauma kit meets the performance standards established by the Director of the Bureau of Justice Assistance under paragraph (3)(A). (B) Authority to separately acquire Nothing in subparagraph (A) shall prohibit a grantee from separately acquiring the components of a trauma kit and assembling complete trauma kits that meet the performance standards. (3) Performance standards and optional agency best practices Not later than 180 days after the date of enactment of this subsection, the Director of the Bureau of Justice Assistance, in consultation with organizations representing trauma surgeons, emergency medical response professionals, emergency physicians, other medical professionals, relevant law enforcement agencies of States and units of local government, professional law enforcement organizations, local law enforcement labor or representative organizations, and law enforcement trade associations, shall\u2014 (A) develop and publish performance standards for trauma kits that are eligible for purchase using funds made available under this part that, at a minimum, require the components described in paragraph (4) to be included in a trauma kit; and (B) develop and publish optional best practices for law enforcement agencies regarding\u2014 (i) training law enforcement officers in the use of trauma kits; (ii) the deployment and maintenance of trauma kits in law enforcement vehicles; and (iii) the deployment, location, and maintenance of trauma kits in law enforcement agency or other government facilities. (4) Components The components of a trauma kit described in this paragraph are\u2014 (A) a tourniquet recommended by the Committee on Tactical Combat Casualty Care; (B) a bleeding control bandage; (C) a pair of nonlatex protective gloves and a pen-type marker; (D) a pair of blunt-ended scissors; (E) instructional documents developed\u2014 (i) under the Stop the Bleed national awareness campaign of the Department of Homeland Security, or any successor thereto; (ii) by the American College of Surgeons Committee on Trauma; (iii) by the American Red Cross; or (iv) by any partner of the Department of Defense; (F) a bag or other container adequately designed to hold the contents of the kit; and (G) any additional trauma kit supplies that\u2014 (i) are approved by a State, local, or Tribal law enforcement agency or first responders; (ii) can adequately treat a traumatic injury; and (iii) can be stored in a readily available kit. .",
      "versionDate": "2025-05-20",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1595es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1595\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo establish standards for trauma kits purchased using funds provided under the Edward Byrne Memorial Justice Assistance Grant Program.\n#### 1. Short title\nThis Act may be cited as the Improving Police Critical Aid for Responding to Emergencies Act or the Improving Police CARE Act .\n#### 2. Trauma kit standards\nSection 521 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10202 ) is amended by adding at the end the following:\n(d) Trauma kits (1) Definition In this subsection, the term trauma kit means a first aid response kit, which includes a bleeding control kit that can be used for controlling a life-threatening hemorrhage. (2) Requirement for trauma kits (A) In general Notwithstanding any other provision of law, a grantee may only purchase a trauma kit using funds made available under this part if the trauma kit meets the performance standards established by the Director of the Bureau of Justice Assistance under paragraph (3)(A). (B) Authority to separately acquire Nothing in subparagraph (A) shall prohibit a grantee from separately acquiring the components of a trauma kit and assembling complete trauma kits that meet the performance standards. (3) Performance standards and optional agency best practices Not later than 180 days after the date of enactment of this subsection, the Director of the Bureau of Justice Assistance, in consultation with organizations representing trauma surgeons, emergency medical response professionals, emergency physicians, other medical professionals, relevant law enforcement agencies of States and units of local government, professional law enforcement organizations, local law enforcement labor or representative organizations, and law enforcement trade associations, shall\u2014 (A) develop and publish performance standards for trauma kits that are eligible for purchase using funds made available under this part that, at a minimum, require the components described in paragraph (4) to be included in a trauma kit; and (B) develop and publish optional best practices for law enforcement agencies regarding\u2014 (i) training law enforcement officers in the use of trauma kits; (ii) the deployment and maintenance of trauma kits in law enforcement vehicles; and (iii) the deployment, location, and maintenance of trauma kits in law enforcement agency or other government facilities. (4) Components The components of a trauma kit described in this paragraph are\u2014 (A) a tourniquet recommended by the Committee on Tactical Combat Casualty Care; (B) a bleeding control bandage; (C) a pair of nonlatex protective gloves and a pen-type marker; (D) a pair of blunt-ended scissors; (E) instructional documents developed\u2014 (i) under the Stop the Bleed national awareness campaign of the Department of Homeland Security, or any successor thereto; (ii) by the American College of Surgeons Committee on Trauma; (iii) by the American Red Cross; or (iv) by any partner of the Department of Defense; (F) a bag or other container adequately designed to hold the contents of the kit; and (G) any additional trauma kit supplies that\u2014 (i) are approved by a State, local, or Tribal law enforcement agency or first responders; (ii) can adequately treat a traumatic injury; and (iii) can be stored in a readily available kit. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-10-28",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5864",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Police CARE Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-06-05T14:24:55Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-05T14:24:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-07T20:10:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119s1595",
          "measure-number": "1595",
          "measure-type": "s",
          "orig-publish-date": "2025-07-29",
          "originChamber": "SENATE",
          "update-date": "2026-04-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1595v55",
            "update-date": "2026-04-20"
          },
          "action-date": "2025-07-29",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Improving Police Critical Aid for Responding to Emergencies Act or the Improving Police CARE Act</strong></p><p>This bill requires the Bureau of Justice Assistance (BJA) within the Department of Justice to develop and publish performance standards for trauma kits that are eligible to be purchased using funds under the Edward Byrne Memorial Justice Assistance Grant program.</p><p>Additionally, the BJA must develop and publish best practices for the use, deployment, and maintenance of trauma kits by law enforcement agencies.</p>"
        },
        "title": "Improving Police CARE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1595.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Improving Police Critical Aid for Responding to Emergencies Act or the Improving Police CARE Act</strong></p><p>This bill requires the Bureau of Justice Assistance (BJA) within the Department of Justice to develop and publish performance standards for trauma kits that are eligible to be purchased using funds under the Edward Byrne Memorial Justice Assistance Grant program.</p><p>Additionally, the BJA must develop and publish best practices for the use, deployment, and maintenance of trauma kits by law enforcement agencies.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s1595"
    },
    "title": "Improving Police CARE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Improving Police Critical Aid for Responding to Emergencies Act or the Improving Police CARE Act</strong></p><p>This bill requires the Bureau of Justice Assistance (BJA) within the Department of Justice to develop and publish performance standards for trauma kits that are eligible to be purchased using funds under the Edward Byrne Memorial Justice Assistance Grant program.</p><p>Additionally, the BJA must develop and publish best practices for the use, deployment, and maintenance of trauma kits by law enforcement agencies.</p>",
      "updateDate": "2026-04-20",
      "versionCode": "id119s1595"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1595is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1595rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1595es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Improving Police CARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T11:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Improving Police CARE Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-07-30T06:38:23Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Improving Police Critical Aid for Responding to Emergencies Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-07-30T06:38:23Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Improving Police Critical Aid for Responding to Emergencies Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Improving Police CARE Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Police CARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T14:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Police Critical Aid for Responding to Emergencies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T14:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish standards for trauma kits purchased using funds provided under the Edward Byrne Memorial Justice Assistance Grant Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T14:18:20Z"
    }
  ]
}
```
