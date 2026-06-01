# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7994?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7994
- Title: HERO Act
- Congress: 119
- Bill type: HR
- Bill number: 7994
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-02T16:52:44Z
- Update date including text: 2026-04-02T16:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7994",
    "number": "7994",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HERO Act",
    "type": "HR",
    "updateDate": "2026-04-02T16:52:44Z",
    "updateDateIncludingText": "2026-04-02T16:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-19T13:01:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7994ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7994\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Ruiz introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a grant program to provide schools with opioid overdose reversal drugs, to direct schools receiving Federal funds to report to certain Federal information systems any distribution of an opioid overdose reversal drug, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Educators Respond to Overdoses Act or the HERO Act .\n#### 2. School grants for opioid overdose reversal drugs\n##### (a) In general\nBeginning not later than 90 days after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use (in this section referred to as the Secretary ), in consultation with the Secretary of Education, shall award grants, on a competitive basis, to eligible entities\u2014\n**(1)**\nto purchase opioid overdose reversal drugs that are approved under section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ); and\n**(2)**\nto develop and implement the educational programming or resources referred to in subsection (b)(2)(C).\n##### (b) Applications\n**(1) In general**\nTo be eligible for a grant under this section, an eligible entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate, which shall include the material required under paragraph (2).\n**(2) Application requirements**\nAn application submitted by an eligible entity under paragraph (1) shall include the following:\n**(A)**\nA description of how the eligible entity will use a grant received under this section.\n**(B)**\nAn assurance that the eligible entity will, in consultation with the local health department, develop and implement\u2014\n**(i)**\nin the case of an eligible entity that is a private school, a comprehensive emergency response plan for the staff of the school; and\n**(ii)**\nin the case of an eligible entity that is a local educational agency, such a plan for the staff of each school that is served by the local educational agency.\n**(C)**\nAn assurance that the eligible entity will develop and implement educational programming or resources (which may include programming or resources developed by the Secretary) to promote student and community knowledge of cardiopulmonary resuscitation (commonly known as CPR ), drug-use prevention and intervention, and emergency responses to drug overdoses.\n##### (c) Priority\nIn awarding grants under this section, the Secretary shall give priority to any eligible entity that is in a city or county with a high rate of drug overdoses involving opioids.\n##### (d) Grant period\nA grant awarded under this section shall be for a period of 1 year.\n##### (e) Reports\n**(1) Grant recipients**\nNot later than 1 year after the date on which the grant period referred to in subsection (d) ends, the recipient of a grant under this section shall submit to the Secretary a report that contains the following:\n**(A)**\nA description of the use the recipient made of the opioid overdose reversal drugs purchased with the grant.\n**(B)**\nA description of the comprehensive emergency response plan referred to in subsection (b)(2)(B).\n**(C)**\nA description of the educational programming or resources referred to in subsection (b)(2)(C).\n**(2) Secretary**\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary, in consultation with the Secretary of Education, shall submit to Congress a report that summarizes all information received by the Secretary in the reports referred to in paragraph (1).\n##### (f) Definitions\nIn this section:\n**(1) Charter school**\nThe term charter school has the meaning given such term in section 4310 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221i ).\n**(2) Elementary school, secondary school, and local educational agency**\nThe terms elementary school , secondary school , and local educational agency have the meanings given such terms, respectively, in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na private elementary school or private secondary school; and\n**(B)**\na local educational agency, including a charter school that is a local educational agency, or a consortium of local educational agencies.\n#### 3. Reporting to Federal information systems of school distribution of opioid overdose reversal drugs\n##### (a) In general\nBeginning not later than 90 days after the date of enactment of this Act, a covered educational institution receiving Federal funds shall submit a description of any distribution of an opioid overdose reversal drug by such institution to\u2014\n**(1)**\nthe National Emergency Medical Services Information System (commonly known as NEMSIS ); and\n**(2)**\nthe Overdose Detection Mapping Application Program of the Washington/Baltimore High Intensity Drug Trafficking Area (commonly known as ODMAP ).\n##### (b) Definitions\nIn this section:\n**(1) Charter school**\nThe term charter school has the meaning given such term in section 4310 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221i ).\n**(2) Covered educational institution**\nThe term covered educational institution means\u2014\n**(A)**\na private elementary school or private secondary school; and\n**(B)**\na local educational agency, including a charter school that is a local educational agency.\n**(3) Elementary school, secondary school, and local educational agency**\nThe terms elementary school , secondary school , and local educational agency have the meanings given such terms, respectively, in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).",
      "versionDate": "2026-03-19",
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
        "name": "Education",
        "updateDate": "2026-04-02T16:52:44Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7994ih.xml"
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
      "title": "HERO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HERO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Educators Respond to Overdoses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to provide schools with opioid overdose reversal drugs, to direct schools receiving Federal funds to report to certain Federal information systems any distribution of an opioid overdose reversal drug, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T07:48:37Z"
    }
  ]
}
```
