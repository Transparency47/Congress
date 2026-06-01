# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3312?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3312
- Title: SERVICE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3312
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-02-24T09:05:50Z
- Update date including text: 2026-02-24T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on the Judiciary.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3312",
    "number": "3312",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001220",
        "district": "5",
        "firstName": "Dale",
        "fullName": "Rep. Strong, Dale W. [R-AL-5]",
        "lastName": "Strong",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "SERVICE Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:50Z",
    "updateDateIncludingText": "2026-02-24T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:03:35Z",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MD"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "LA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AL"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NH"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "VA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CO"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "PA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "AL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "OH"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3312ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3312\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Strong (for himself, Mr. Correa , Ms. Salazar , Mr. Ivey , Mr. Higgins of Louisiana , Mr. Valadao , Mr. Moore of Alabama , Mr. Tran , Mr. Davis of North Carolina , Mr. Scott Franklin of Florida , Mr. Rogers of Alabama , Mr. Goldman of New York , and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Attorney General to make grants for the creation and operation of veterans response teams within law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Every at-Risk Veteran In Critical Emergencies Act of 2025 or the SERVICE Act of 2025 .\n#### 2. Veteran Response Team Pilot Program\n##### (a) Grant authorization\nThe Attorney General, acting through the Director of the Office of Community Oriented Policing Services, is authorized to operate a pilot program to make grants to States, units of local government, and Indian Tribal governments, to support the creation and operation of veterans response teams in the law enforcement agencies of the jurisdiction, in accordance with subsection (b).\n##### (b) Grants To develop veterans response teams\n**(1) Activities of a veterans response team**\nA veterans response team may include a program that does the following:\n**(A)**\nProvides law enforcement officers who are veterans with a pin that identifies the department of the Armed Forces in which the officer served, which the officer may wear while on duty.\n**(B)**\nUses the Veterans Re-Entry Search Service of the Department of Veterans Affairs.\n**(C)**\nEstablishes a system of communication and information sharing with the Department of Veterans Affairs and other community resource agencies.\n**(D)**\nEstablishes a working relationship with the Veterans Justice Outreach specialist.\n**(E)**\nEstablishes a working relationship with the local justice system and veterans court, if applicable, including identifying veterans upon entry into the court system and local detention facility, with notification to the local Department of Veterans Affairs office for confirmation and appropriate services.\n**(F)**\nProvides training and education for law enforcement officers on mental health issues related to military service, such as post-traumatic stress disorder, traumatic brain injury, depression, and anxiety.\n**(G)**\nMeets regularly to discuss issues veterans are facing in the community, as well as suitable responses.\n**(H)**\nOrganizes coordinated and trained teams of first responders to respond 24 hours per day, and 7 days per week, on a volunteer basis, to calls for assistance involving a veteran in crisis.\n**(I)**\nDevelops a plan to\u2014\n**(i)**\nmeasure the success of veteran response teams; and\n**(ii)**\ntrack nationwide best practices on how veterans response teams provide law enforcement officers with essential information during and following veteran-involved incidents to which veterans response teams respond.\n**(J)**\nOffers veterans who have come into contact with the veterans response team the opportunity to maintain ongoing contact with the veterans response team.\n**(2) Creation, Hiring, and Training of Veterans Response Team**\nThe creation of a veterans response team within a law enforcement agency pursuant to a grant under this section may include doing the following:\n**(A)**\nIdentifying a law enforcement officer in the law enforcement agency who is passionate about and committed to forming a veterans response team, and will serve as the leader of such team.\n**(B)**\nIdentifying other law enforcement officers in the law enforcement agency who are interested and willing to participate on the veterans response team.\n**(C)**\nIdentifying and inviting interested community members to join the veterans response team, which may include members of veteran resource organizations, the local office of the Department of Veterans Affairs, the regional veterans justice outreach program, other law enforcement agencies, fire and emergency medical services departments, hospitals, social work agencies, other entities within the justice system, nonprofit organizations, and other appropriate entities.\n**(D)**\nImmersing veterans response team members in the veteran community by attending veterans events, responding to incidents involving veterans, as described in paragraph (1)(I), and making public appearances to further engage with veterans.\n**(E)**\nProviding training on veterans experiencing crisis for individuals involved with the veterans response team, and for other law enforcement officers who are likely to come in contact with veterans.\n##### (c) Termination\nThe authority under this section shall terminate on the date that is 5 years after the date of the enactment of this section.\n##### (d) Reporting\nThe Attorney General shall provide a report to Congress on the progress of the pilot program that includes the following:\n**(1)**\nThe number of applicants.\n**(2)**\nThe number of grants awarded.\n**(3)**\nThe average grant amount sought by an applicant.\n**(4)**\nThe average amount of a grant awarded.\n**(5)**\nAny other information that the Attorney General determines to be appropriate.\n##### (e) Funds\nSubject to the availability of appropriations, the pilot program under this section shall be carried out using funds made available for grants under part Q of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 et seq. ) for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-05-08",
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
        "updateDate": "2025-05-22T17:25:10Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3312ih.xml"
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
      "title": "SERVICE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SERVICE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Every at-Risk Veteran In Critical Emergencies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Attorney General to make grants for the creation and operation of veterans response teams within law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:28Z"
    }
  ]
}
```
