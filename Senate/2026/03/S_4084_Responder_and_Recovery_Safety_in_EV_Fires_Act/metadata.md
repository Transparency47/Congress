# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4084?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4084
- Title: Responder and Recovery Safety in EV Fires Act
- Congress: 119
- Bill type: S
- Bill number: 4084
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-24T18:01:40Z
- Update date including text: 2026-04-24T18:01:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4084",
    "number": "4084",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Responder and Recovery Safety in EV Fires Act",
    "type": "S",
    "updateDate": "2026-04-24T18:01:40Z",
    "updateDateIncludingText": "2026-04-24T18:01:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T17:27:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4084is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4084\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Sheehy (for himself and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Transportation to establish a working group to review and establish guidance and best practices for responding to electric vehicle fires, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responder and Recovery Safety in EV Fires Act .\n#### 2. Electric Vehicle Fire Response Working Group\n##### (a) Definitions\nIn this section:\n**(1) Electric vehicle**\nThe term electric vehicle means a car, bus, or truck, including an automobile or commercial medium- or heavy-duty on-highway vehicle (as those terms are defined in section 32901(a) of title 49, United States Code), that\u2014\n**(A)**\nis manufactured primarily for use on public roads or highways; and\n**(B)**\ncontains a battery or similar energy storage device that provides motive power to propel the car, bus, or truck.\n**(2) Public road**\nThe term public road has the meaning given the term in section 101(a) of title 23, United States Code.\n**(3) Roadside incident**\nThe term roadside incident means an incident involving an electric vehicle that occurs on a public road or any area adjacent to a public road as a result of the use of the electric vehicle on the public road, including\u2014\n**(A)**\non the shoulder or median of a public road;\n**(B)**\nat a charging station for electric vehicles that is open to the public; and\n**(C)**\non a parking deck or lot that is open to the public.\n**(4) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(5) Working group**\nThe term working group means the Electric Vehicle Fire Response Working Group established under subsection (b).\n##### (b) Establishment\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a working group, to be known as the Electric Vehicle Fire Response Working Group .\n##### (c) Composition\nThe working group shall be composed of not fewer than 22 members, including\u2014\n**(1)**\nat least 2 representatives of the towing industry, appointed by the Secretary from among individuals nominated by appropriate entities operating in or representing the towing industry, including\u2014\n**(A)**\nif nominated, at least 2 representatives nominated by the Towing and Recovery Association of America (commonly known as the TRAA ); and\n**(B)**\nsuch other representatives of the towing industry as the Secretary determines to be appropriate;\n**(2)**\nat least 6 representatives of emergency response personnel, appointed by the Secretary from among individuals nominated by appropriate entities representing emergency response personnel who may respond to electric vehicle fires, including\u2014\n**(A)**\nif nominated\u2014\n**(i)**\nat least 1 representative nominated by the International Association of Fire Chiefs (commonly known as the IAFC );\n**(ii)**\nat least 1 representative nominated by the International Association of Fire Fighters (commonly known as the IAFF );\n**(iii)**\nat least 1 representative nominated by the National Volunteer Fire Council (commonly known as the NVFC );\n**(iv)**\nat least 1 representative nominated by the International Association of Chiefs of Police (commonly known as the IACP );\n**(v)**\nat least 1 representative nominated by the National Association of State Emergency Medical Services Officials (commonly known as the NASEMSO ); and\n**(vi)**\nat least 1 representative nominated by the American Public Works Association (commonly known as the APWA ); and\n**(B)**\nsuch other representatives of emergency response personnel as the Secretary determines to be appropriate;\n**(3)**\nat least 6 representatives of the automotive industry, appointed by the Secretary from among individuals nominated by appropriate entities operating in or representing original equipment manufacturers of electric vehicles or the component parts of electric vehicles, including\u2014\n**(A)**\nif nominated\u2014\n**(i)**\nat least 1 representative nominated by the Zero Emission Transportation Association (commonly known as the ZETA );\n**(ii)**\nat least 1 representative of manufacturers of electric buses;\n**(iii)**\nat least 1 representative of manufacturers of electric commercial medium- or heavy-duty on-highway vehicles;\n**(iv)**\nat least 1 representative of manufacturers of electric vehicle batteries;\n**(v)**\nat least 1 representative of manufacturers or installers of electric vehicle supply equipment; and\n**(vi)**\nat least 1 representative of manufacturers of electric vehicles; and\n**(B)**\nsuch other representatives of the electric vehicle manufacturing industry as the Secretary determines to be appropriate;\n**(4)**\nat least 4 representatives of research, standards-setting, or training organizations with expertise relating to the risks of electric vehicle fires and electric vehicle fire response, including\u2014\n**(A)**\nif nominated\u2014\n**(i)**\nat least 1 representative nominated by the National Fire Protection Association (commonly known as the NFPA );\n**(ii)**\nat least 1 representative nominated by the Emergency Responder Safety Institute (commonly known as the ERSI );\n**(iii)**\nat least 1 representative nominated by the Fire Safety Research Institute of UL Research Institutes (commonly known as UL\u2013FSRI ); and\n**(iv)**\nat least 1 representative nominated by the Society of Automotive Engineers International (commonly known as the SAE ); and\n**(B)**\nsuch other representatives of research, standards-setting, or training organizations as the Secretary determines to be appropriate;\n**(5)**\n1 representative of the National Transportation Safety Board, appointed by the National Transportation Safety Board;\n**(6)**\n1 representative of the National Highway Traffic Safety Administration, appointed by the Secretary, acting through the Administrator of the National Highway Traffic Safety Administration;\n**(7)**\n1 representative of the Federal Highway Administration, appointed by the Secretary, acting through the Administrator of the Federal Highway Administration;\n**(8)**\n1 representative of the United States Fire Administration, appointed by the Administrator of the United States Fire Administration; and\n**(9)**\nsuch other representatives of a Federal agency as the Secretary determines to be appropriate, such as representatives of\u2014\n**(A)**\nthe Department of Transportation (including any relevant agency or modal administration of the Department of Transportation);\n**(B)**\nthe Department of Energy;\n**(C)**\nthe intelligence community (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )); or\n**(D)**\nFederal law enforcement agencies.\n##### (d) Head\nThe Secretary shall select 1 member of the working group to serve as head of the working group.\n##### (e) Compensation\nMembers of the working group shall serve without compensation.\n##### (f) Duties\nThe working group shall\u2014\n**(1)**\ncontinuously review\u2014\n**(A)**\nknown and developing risks relating to electric vehicle fires and electric vehicle fire response;\n**(B)**\nexisting best practices, standards, and guidance relating to electric vehicle fire response; and\n**(C)**\nroadside incidents involving electric vehicle fires, including any response procedures utilized; and\n**(2)**\nbased on that review, periodically issue or update best practices and guidance for responding to electric vehicle fires.\n##### (g) Database\n**(1) In general**\nThe working group shall\u2014\n**(A)**\nreport roadside incidents involving electric vehicle fires for inclusion in the database established and maintained pursuant to section 9 of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2208 ) (also known as the National Emergency Response Information System or the NERIS ); and\n**(B)**\ncoordinate with the United States Fire Administration to maintain and update that database, including by ensuring that the database includes, to the maximum extent practicable, the information described in paragraph (3) with respect to roadside incidents.\n**(2) Publication**\nThe Administrator of the United States Fire Administration shall publish the information in the reports required by paragraph (1) in the database described in that paragraph.\n**(3) Contents**\nTo the maximum extent practicable, the reports required by paragraph (1) shall include, with respect to each roadside incident reported\u2014\n**(A)**\nthe location of the incident;\n**(B)**\nthe time of the incident and response;\n**(C)**\nthe conditions at the scene, such as\u2014\n**(i)**\nthe weather;\n**(ii)**\nthe presence or absence of daylight;\n**(iii)**\nthe presence or absence of passengers, pedestrians, or other vehicles; and\n**(iv)**\nsuch other conditions as the working group determines to be relevant;\n**(D)**\nthe practices and procedures used to respond to the electric vehicle fire;\n**(E)**\nthe results of the incident and response; and\n**(F)**\nsuch other information relating to a roadside incident as the working group determines to be appropriate.\n##### (h) Annual report\nThe working group shall submit to Congress and make publicly available an annual report on the work of the working group during the previous year, including\u2014\n**(1)**\na summary of any best practices and guidance issued or updated; and\n**(2)**\na summary of any issues for which new or updated best practices or guidance is being considered.\n##### (i) FACA\nChapter 10 of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ), shall not apply to the working group.\n##### (j) Administrative expenses\n**(1) In general**\nThe Secretary shall provide administrative support for the working group in a manner consistent with the provision of support services under section 1011 of title 5, United States Code.\n**(2) Funding**\nThe Secretary shall use existing funds available to the Secretary to carry out paragraph (1).\n##### (k) Termination\nThe working group shall terminate on the date that is 10 years after the date on which the working group is established under subsection (b).",
      "versionDate": "2026-03-12",
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
        "actionDate": "2026-04-15",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "8307",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Responder and Recovery Safety in EV Fires Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-01T19:11:29Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4084is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Transportation to establish a working group to review and establish guidance and best practices for responding to electric vehicle fires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:24Z"
    },
    {
      "title": "Responder and Recovery Safety in EV Fires Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Responder and Recovery Safety in EV Fires Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
