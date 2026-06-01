# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4882?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4882
- Title: Gun Safety Board and Research Act
- Congress: 119
- Bill type: HR
- Bill number: 4882
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-09-18T17:52:40Z
- Update date including text: 2025-09-18T17:52:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4882",
    "number": "4882",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000623",
        "district": "10",
        "firstName": "Mark",
        "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
        "lastName": "DeSaulnier",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Gun Safety Board and Research Act",
    "type": "HR",
    "updateDate": "2025-09-18T17:52:40Z",
    "updateDateIncludingText": "2025-09-18T17:52:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:00:05Z",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4882ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4882\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. DeSaulnier introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a Gun Safety Board, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gun Safety Board and Research Act .\n#### 2. Gun Safety Board\n##### (a) Establishment\nThe Secretary of Health and Human Services shall, not later than 1 year after the date of enactment of this Act, establish a board to be known as the Gun Safety Board.\n##### (b) Duties\nThe Gun Safety Board shall\u2014\n**(1)**\nnot later than 2 years after the date of enactment of this Act, establish a program that uses not less than half of the amounts appropriated under this Act to provide grants that recipients shall use to\u2014\n**(A)**\nconduct original research about firearm violence reduction (including research about topics identified for additional research by the Gun Safety Board under paragraph (3)); and\n**(B)**\neducate members of the public about\u2014\n**(i)**\ncauses and effects of firearm violence; and\n**(ii)**\nways to reduce firearm violence;\n**(2)**\nconduct original research about firearm violence reduction; and\n**(3)**\npublish in the Federal Register and on a public website of the Department of Health and Human Services, not less frequently than annually\u2014\n**(A)**\npolicy and funding recommendations for potential Federal, State, and local action based on available scientific research about firearm violence reduction;\n**(B)**\na list of subject areas related to firearm violence reduction that the Gun Safety Board finds would benefit from additional scientific research; and\n**(C)**\nthe Gun Safety Board\u2019s findings about the efficacy of existing State and Federal laws intended to reduce firearm violence, and the expected efficacy of proposed State and Federal legislation intended to reduce firearm violence, in reducing\u2014\n**(i)**\ndomestic violence;\n**(ii)**\nsuicide and attempted suicide;\n**(iii)**\nchronic community violence;\n**(iv)**\npolice violence;\n**(v)**\nmass shootings;\n**(vi)**\nhate crimes;\n**(vii)**\nschool shootings;\n**(viii)**\nhealth care-related expenditures (including lost days of work and other indirect expenditures) for victims of firearm-caused injuries;\n**(ix)**\nhospital interventions;\n**(x)**\nbroader socioeconomic impacts of chronic gun violence;\n**(xi)**\ndiversions of firearms, including straw purchasing and gun trafficking; and\n**(xii)**\nunintentional shootings.\n##### (c) Membership\n**(1) Number and appointment**\nThe Gun Safety Board shall be composed of 22 members appointed by the Secretary of Health and Human Services.\n**(2) Composition**\nThe members shall include\u2014\n**(A)**\n1 member with expertise in public health;\n**(B)**\n1 member with expertise in mental health care;\n**(C)**\n1 member with expertise in firearm violence reduction research;\n**(D)**\n1 member with expertise in trauma surgery;\n**(E)**\n1 member with expertise in law enforcement;\n**(F)**\n1 member with a background in firearm manufacturing, firearm sales, professional firearm use, or recreational firearm use;\n**(G)**\n2 members representing victims of firearm violence;\n**(H)**\n1 member representing a nonprofit organization that advocates for racial justice;\n**(I)**\n1 member representing a nonprofit organization that advocates or engages in firearm violence intervention or prevention; and\n**(J)**\n1 member from each of\u2014\n**(i)**\nthe National Institutes of Health;\n**(ii)**\nthe Centers for Disease Control and Prevention;\n**(iii)**\nthe Substance Abuse and Mental Health Services Administration;\n**(iv)**\nthe United States Consumer Product Safety Commission;\n**(v)**\nthe Federal Bureau of Investigation;\n**(vi)**\nthe Department of Health and Human Services;\n**(vii)**\nthe Bureau of Alcohol, Tobacco, Firearms and Explosives within the Department of Justice;\n**(viii)**\nthe Office of Juvenile Justice and Delinquency Prevention within the Department of Justice;\n**(ix)**\nthe Bureau of Justice Assistance within the Department of Justice;\n**(x)**\nthe Office for Victims of Crime within the Department of Justice;\n**(xi)**\nthe Office on Violence Against Women within the Department of Justice; and\n**(xii)**\nthe National Institute of Justice within the Department of Justice.\n##### (d) Terms\n**(1) In general**\nExcept as provided in paragraph (2), each member shall be appointed for a term of 4 years.\n**(2) Terms of initial appointees**\nAs designated by the Secretary of Health and Human Services at the time of appointment, of the members first appointed\u2014\n**(A)**\n7 shall be appointed for a term of 4 years;\n**(B)**\n6 shall be appointed for a term of 3 years;\n**(C)**\n5 shall be appointed for a term of 2 years; and\n**(D)**\n4 shall be appointed for a term of 1 year.\n**(3) Vacancies**\nAny member appointed to fill a vacancy occurring before the expiration of the term for which the member\u2019s predecessor was appointed shall be appointed only for the remainder of that term. A vacancy shall be filled in the manner in which the original appointment was made.\n##### (e) Basic pay\nMembers shall be paid at a rate set by the Secretary of Health and Human Services that is consistent with title 5, United States Code.\n##### (f) Travel expenses\nEach member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n##### (g) Chair\nThe Secretary of Health and Human Services shall designate 1 member to serve as chair of the Gun Safety Board.\n##### (h) Vice Chair\nThe members of the Gun Safety Board shall elect 1 member to serve as vice chair of the Gun Safety Board.\n##### (i) Meetings\nThe Board shall meet at least once each month at the call of the chair.\n##### (j) Staff\nThe chair may appoint and, consistent with title 5, United States Code, fix the pay of additional personnel as the chair considers appropriate.\n##### (k) Firearm\nFor the purposes of this Act, the term firearm shall have the meaning given the term in section 921 of title 18, United States Code.\n##### (l) Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $5,000,000 for each of the first 2 fiscal years beginning after the date of the enactment of this Act, and $25,000,000 for each fiscal year thereafter.\n##### (m) Prohibition on diversion of other Federal gun violence research funds\nThe amounts made available for Federal gun violence research other than under this Act shall not be reduced in order to provide funds to carry out this Act.",
      "versionDate": "2025-08-05",
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
        "name": "Health",
        "updateDate": "2025-09-18T17:52:40Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4882ih.xml"
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
      "title": "Gun Safety Board and Research Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gun Safety Board and Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Gun Safety Board, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:34Z"
    }
  ]
}
```
