# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8886
- Title: SMART Community Policing Act
- Congress: 119
- Bill type: HR
- Bill number: 8886
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-30T04:53:26Z
- Update date including text: 2026-05-30T04:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8886",
    "number": "8886",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "SMART Community Policing Act",
    "type": "HR",
    "updateDate": "2026-05-30T04:53:26Z",
    "updateDateIncludingText": "2026-05-30T04:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
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
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
          "date": "2026-05-19T16:05:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8886ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8886\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mr. Crow introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for innovations in community policing, mental health care, and community safety, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Mental Assistance Responder Teams Community Policing Act or the SMART Community Policing Act .\n#### 2. Purpose\nThe purpose of this Act is to strengthen community policing programs to\u2014\n**(1)**\nde-escalate interactions with law enforcement officers to achieve better outcomes for non-violent individuals experiencing crisis or trauma relating to mental health issues, poverty, homelessness, and substance use disorders;\n**(2)**\nbuild collaborative partnerships to connect individuals with mental health services and community resources; and\n**(3)**\nproduce better outcomes for communities and law enforcement officers by delivering the appropriate treatment and other support services to individuals in need.\n#### 3. Additional authorized uses of COPS funds\nSection 1701(b) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381(b) ) is amended\u2014\n**(1)**\nin paragraph (24), by striking and at the end;\n**(2)**\nin paragraph (25), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(26) to establish or expand a mobile crisis team program to\u2014 (A) hire skilled mental health professionals and paramedics to\u2014 (i) respond to\u2014 (I) certain 911 dispatch calls at the request of law enforcement officers; and (II) community members requesting assistance directly; (ii) stabilize encounters between law enforcement officers and individuals experiencing a mental or behavioral health crisis; and (iii) assume responsibility for securing mental health services for individuals, including individuals in crisis who may need further evaluation and treatment; (B) train law enforcement officers partnering with mental health professionals and paramedics; (C) use a mobile unit to facilitate the response of law enforcement officers and mental health professionals and paramedics to community members experiencing a mental or behavioral health crisis; and (D) hire other personnel; (27) to establish or expand a co-responder program under which\u2014 (A) a trained law enforcement officer is paired with a behavioral health clinician or paramedic to\u2014 (i) de-escalate situations involving a mental health crisis; (ii) connect individuals with mental illness to appropriate services; and (iii) provide other effective and efficient responses to individuals with mental illness; and (B) additional personnel, including law enforcement officers and case managers, may be hired; and (28) to establish or expand a case management and outreach team\u2014 (A) to follow up with individuals experiencing a mental or behavioral health crisis to\u2014 (i) connect those individuals with mental health services and community resources; and (ii) help those individuals abide by treatment plans and meet other responsibilities, such as work, school, and training; (B) to develop specific solutions for, and provide support resources to, individuals who frequently use emergency services to reduce repeat interactions between the individuals described in subparagraph (A) and law enforcement officers or mental health professionals and paramedics; and (C) which may be established as a part of a mobile crisis team program under paragraph (26), a co-responder program under paragraph (27), or an independent team. .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8886ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SMART Community Policing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Mental Assistance Responder Teams Community Policing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "title": "SMART Community Policing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for innovations in community policing, mental health care, and community safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T04:48:27Z"
    }
  ]
}
```
