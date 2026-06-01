# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1466
- Title: Resources for Victims of Gun Violence Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1466
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-05T21:50:15Z
- Update date including text: 2025-12-05T21:50:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1466",
    "number": "1466",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Resources for Victims of Gun Violence Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:50:15Z",
    "updateDateIncludingText": "2025-12-05T21:50:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T19:40:54Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NM"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1466is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1466\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Markey (for himself, Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Heinrich , Ms. Klobuchar , Mr. Murphy , Mr. Padilla , Ms. Rosen , Mrs. Shaheen , Mr. Van Hollen , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a Federal Advisory Council to Support Victims of Gun Violence.\n#### 1. Short title\nThis Act may be cited as the Resources for Victims of Gun Violence Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Advisory council**\nThe term Advisory Council means the Advisory Council to Support Victims of Gun Violence established under section 3.\n**(2) Appropriate committees**\nThe term appropriate committees means the following:\n**(A)**\nThe Committee on Health, Education, Labor, and Pensions of the Senate.\n**(B)**\nThe Committee on the Judiciary of the Senate.\n**(C)**\nThe Committee on Education and Workforce of the House of Representatives.\n**(D)**\nThe Committee on Energy and Commerce of the House of Representatives.\n**(E)**\nThe Committee on the Judiciary of the House of Representatives.\n**(F)**\nAny other relevant committee of the Senate or of the House of Representatives with jurisdiction over matters affecting victims of gun violence.\n**(3) Gun violence**\nThe term gun violence means\u2014\n**(A)**\nsuicide involving firearms;\n**(B)**\nhomicide involving firearms;\n**(C)**\ndomestic violence involving firearms;\n**(D)**\nhate crimes involving firearms;\n**(E)**\nyouth violence involving firearms;\n**(F)**\nmass shootings;\n**(G)**\nunintentional shootings;\n**(H)**\nnon-fatal shootings; and\n**(I)**\nthreats or exposure to violent acts involving firearms.\n**(4) Victim assistance professional**\nThe term victim assistance professional means a professional who assists victims of gun violence, including\u2014\n**(A)**\na medical professional, including an emergency medical professional;\n**(B)**\na social worker;\n**(C)**\na provider of long-term services or care; and\n**(D)**\na victim advocate.\n**(5) Victim of gun violence**\nThe term victim of gun violence means\u2014\n**(A)**\nan individual who has been wounded as a result of gun violence;\n**(B)**\nan individual who has been threatened with an act of gun violence;\n**(C)**\nan individual who has witnessed an act of gun violence; and\n**(D)**\na relative, classmate, coworker, or other associate of\u2014\n**(i)**\nan individual who has been killed as a result of gun violence; or\n**(ii)**\nan individual described in subparagraph (A) or (B).\n#### 3. Advisory Council to Support Victims of Gun Violence\n##### (a) Establishment\nThere is established an Advisory Council to Support Victims of Gun Violence.\n##### (b) Membership\n**(1) In general**\nThe Advisory Council shall be composed of the following members or their designees:\n**(A)**\nThe Secretary of Health and Human Services.\n**(B)**\nThe Attorney General.\n**(C)**\nThe Secretary of Education.\n**(D)**\nThe Secretary of Housing and Urban Development.\n**(E)**\nThe Secretary of Veterans Affairs.\n**(F)**\nThe Commissioner of Social Security.\n**(G)**\nThe Assistant Secretary for Mental Health and Substance Use.\n**(H)**\nThe Director of the Centers for Disease Control and Prevention.\n**(I)**\nThe Director of the National Institutes of Health.\n**(J)**\nThe Administrator of the Administration for Community Living.\n**(K)**\nThe Director of the Office on Violence Against Women.\n**(L)**\nThe Director of the Office for Victims of Crime.\n**(M)**\nThe chairman of the Board of the Legal Services Corporation.\n**(N)**\nAs appropriate, the head of any other Federal department or agency identified by the Secretary of Health and Human Services as having responsibilities, or administering programs, relating to issues affecting victims of gun violence.\n**(2) Additional members**\nIn addition to the members described in paragraph (1), the Advisory Council shall be composed of the following:\n**(A)**\nNot fewer than 2 and not more than 5 victims of gun violence, who shall be appointed by the Secretary of Health and Human Services.\n**(B)**\nNot fewer than 2 and not more than 5 victim assistance professionals, who shall be appointed by the Secretary of Health and Human Services.\n**(3) Lead agency**\nThe Department of Health and Human Services shall be the lead agency for the Advisory Council.\n##### (c) Duties\n**(1) Assessment**\nThe Advisory Council shall\u2014\n**(A)**\nsurvey victims of gun violence and victim assistance professionals about their needs in order to inform the content of information disseminated under paragraph (2) and the report published under paragraph (3);\n**(B)**\nconduct a literature review and assess past or ongoing programs designed to assist victims of gun violence or individuals with similar needs to determine\u2014\n**(i)**\nthe effectiveness of the programs; and\n**(ii)**\nbest and promising practices for assisting victims of gun violence; and\n**(C)**\nassess the administration of compensation funds established after mass shootings to determine best and promising practices to direct victims of gun violence to sources of funding.\n**(2) Information**\n**(A) In general**\nThe Advisory Council shall identify, promote, coordinate, and disseminate to the public information, resources, and best and promising practices available to help victims of gun violence\u2014\n**(i)**\nmeet their medical, financial, educational, workplace, housing, transportation, assistive technology, and accessibility needs;\n**(ii)**\nmaintain their mental health and emotional well-being;\n**(iii)**\nseek legal redress for their injuries and protection against any ongoing threats to their safety; and\n**(iv)**\naccess government programs, services, and benefits for which they may be eligible or to which they may be entitled.\n**(B) Contact information**\nThe Advisory Council shall include in the information disseminated under subparagraph (A) the websites and telephone contact information for helplines of relevant Federal agencies, State agencies, and nonprofit organizations.\n**(C) Availability**\nThe Advisory Council shall make the information described in subparagraphs (A) and (B) available\u2014\n**(i)**\nonline through a public website; and\n**(ii)**\nby submitting a hard copy and making available additional hard copies to\u2014\n**(I)**\neach Member of Congress;\n**(II)**\neach field office of the Social Security Administration;\n**(III)**\neach State agency that is responsible for administering health and human services, for dissemination to medical facilities;\n**(IV)**\neach State agency that is responsible for administering education programs, for dissemination to schools; and\n**(V)**\nthe office of each State attorney general, for dissemination to local prosecutor's offices.\n**(3) Report**\nNot later than 180 days after the date of enactment of this Act, the Advisory Council shall\u2014\n**(A)**\nprepare a report that\u2014\n**(i)**\nincludes the best and promising practices, resources, and other useful information for victims of gun violence identified under paragraph (2);\n**(ii)**\nidentifies any gaps in items described in clause (i); and\n**(iii)**\nif applicable, identifies any additional Federal or State legislative authority necessary to implement the activities described in clause (i) or address the gaps described in clause (ii);\n**(B)**\nsubmit the report prepared under subparagraph (A) to\u2014\n**(i)**\nthe appropriate committees;\n**(ii)**\neach State agency that is responsible for administering health and human services;\n**(iii)**\neach State agency that is responsible for administering education programs; and\n**(iv)**\nthe office of each State attorney general; and\n**(C)**\nmake the report prepared under subparagraph (A) available to the public online in an accessible format.\n**(4) Follow-up report**\nNot later than 2 years after the date on which the Advisory Council prepares the report under paragraph (3), the Advisory Council shall\u2014\n**(A)**\nsubmit to the entities described in subparagraph (B) of that paragraph a follow-up report that includes the information identified in subparagraph (A) of that paragraph; and\n**(B)**\nmake the follow-up report described in subparagraph (A) available to the public online in an accessible format.\n**(5) Public input**\n**(A) In general**\nThe Advisory Council shall establish a process to collect public input to inform the development of, and provide updates to, the best and promising practices, resources, and other information described in paragraph (2), including by conducting outreach to entities and individuals described in subparagraph (B) of this paragraph that\u2014\n**(i)**\nhave a range of experience with the types of gun violence described in section 2(3); and\n**(ii)**\ninclude representation from communities disproportionately affected by gun violence.\n**(B) Entities and individuals**\nThe entities and individuals described in this subparagraph are\u2014\n**(i)**\nStates, local governments, and organizations that provide information to, or support for, victims of gun violence;\n**(ii)**\nvictims of gun violence; and\n**(iii)**\nvictim assistance professionals.\n**(C) Nature of outreach**\nIn conducting outreach under subparagraph (A), the Advisory Council shall ask for input on\u2014\n**(i)**\ninformation, resources, and best and promising practices available, including identification of any gaps and unmet needs;\n**(ii)**\nrecommendations that would help victims of gun violence\u2014\n**(I)**\nbetter meet their medical, financial, educational, workplace, housing, transportation, assistive technology, and accessibility needs;\n**(II)**\nmaintain their mental health and emotional well-being;\n**(III)**\nseek legal redress for their injuries and protection against any ongoing threats to their safety; and\n**(IV)**\naccess government programs, services, and benefits for which the victims may be eligible or to which the victims may be entitled; and\n**(iii)**\nany other subject areas discovered during the process that would help victims of gun violence.\n##### (d) Federal Advisory Committee Act\nChapter 10 of title 5, United States Code, shall not apply to the Advisory Council.\n##### (e) Funding\nNo additional funds are authorized to be appropriated to carry out this Act.\n##### (f) Sunset\nThe Advisory Council shall terminate on the date that is 5 years after the date of enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2837",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Resources for Victims of Gun Violence Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-20T12:18:12Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1466is.xml"
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
      "title": "Resources for Victims of Gun Violence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Resources for Victims of Gun Violence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T02:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Federal Advisory Council to Support Victims of Gun Violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:24Z"
    }
  ]
}
```
