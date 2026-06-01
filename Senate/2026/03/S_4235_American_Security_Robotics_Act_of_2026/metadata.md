# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4235
- Title: American Security Robotics Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4235
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-20T23:35:16Z
- Update date including text: 2026-04-20T23:35:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4235",
    "number": "4235",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "American Security Robotics Act of 2026",
    "type": "S",
    "updateDate": "2026-04-20T23:35:16Z",
    "updateDateIncludingText": "2026-04-20T23:35:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T18:09:21Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4235is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4235\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Cotton (for himself and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit executive agencies from procuring or operating certain unmanned ground vehicle systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Security Robotics Act of 2026 .\n#### 2. Prohibition on the procurement and operation of covered unmanned ground vehicle systems\n##### (a) Definitions\nIn this section:\n**(1) Covered nation**\nThe term covered nation has the meaning given the term in section 4872(f) of title 10, United States Code.\n**(2) Covered foreign entity**\nThe term covered foreign entity means an entity that is\u2014\n**(A)**\ndomiciled in a covered nation;\n**(B)**\nsubject to the influence or control of the government of a covered nation, as determined by the Secretary of Homeland Security or the Secretary of Defense; or\n**(C)**\na subsidiary or affiliate of an entity described in subparagraph (A) or (B).\n**(3) Covered unmanned ground vehicle system**\nThe term covered unmanned ground vehicle system means an unmanned ground vehicle system manufactured or assembled by a covered foreign entity.\n**(4) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(5) Unmanned ground vehicle system**\nThe term unmanned ground vehicle system means a system that includes\u2014\n**(A)**\na mechanical device, including a remote surveillance vehicle, autonomous patrol technology, mobile robotics, or a humanoid robot, that\u2014\n**(i)**\nis capable of locomotion, navigation, or movement on the ground; and\n**(ii)**\noperates at a distance from a human operator or supervisor based on commands or in response to sensor data or any combination thereof;\n**(B)**\nthe payload of the mechanical device described in subparagraph (A); and\n**(C)**\nany external device used to control the mechanical device described in subparagraph (A).\n##### (b) Prohibition on procurement of covered unmanned ground vehicle systems\nExcept as provided under subsection (e), the head of an executive agency may not procure any covered unmanned ground vehicle system.\n##### (c) Prohibition on operation of covered unmanned ground vehicle systems\n**(1) In general**\nExcept as provided in subsection (e), beginning on the date that is one year after the date of the enactment of this Act, no executive agency may operate a covered unmanned ground vehicle system.\n**(2) Applicability to contracted services**\nThe prohibition under paragraph (1) applies to any covered unmanned ground vehicle system being used by an executive agency through a contract for the services of the covered unmanned ground vehicle system.\n##### (d) Prohibition on use of Federal funds for procurement or operation of covered unmanned ground vehicle systems\nExcept as provided in subsection (e), beginning on the date that is one year after the date of the enactment of this Act, no Federal funds awarded through a contract, grant, or cooperative agreement, or otherwise made available, may be used to procure or in connection with the operation of a covered unmanned ground vehicle system.\n##### (e) Exemption to prohibitions\n**(1) In general**\nThe head of an agency described in paragraph (2) is exempt from the prohibitions under subsections (b), (c), and (d) if\u2014\n**(A)**\nthe procurement or operation of the covered unmanned ground vehicle system is in the national interest of the United States; and\n**(B)**\n**(i)**\nthe sole purpose for the procurement or operation is\u2014\n**(I)**\nresearch, evaluation, training, testing, or analysis for electronic warfare, information warfare operations, cybersecurity, or the development of unmanned ground vehicle system or counter-unmanned ground vehicle system technology; or\n**(II)**\nconducting counter-terrorism or counterintelligence activities, protective missions, or Federal criminal or national security investigations, including forensic examinations; or\n**(ii)**\nthe covered unmanned ground vehicle system, as procured or as modified after procurement but before operational use\u2014\n**(I)**\ncan no longer transfer data to, or download data from, a covered foreign entity; and\n**(II)**\nposes no national security cybersecurity risk as determined by the head of the agency.\n**(2) Agencies described**\nThe agencies described in this paragraph are\u2014\n**(A)**\nthe Department of Homeland Security;\n**(B)**\nthe Department of Defense;\n**(C)**\nthe Department of State; and\n**(D)**\nthe Department of Justice.",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-04-02",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "8189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Security Robotics Act of 2026",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-20T23:35:15Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4235is.xml"
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
      "title": "American Security Robotics Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Security Robotics Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit executive agencies from procuring or operating certain unmanned ground vehicle systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:32Z"
    }
  ]
}
```
