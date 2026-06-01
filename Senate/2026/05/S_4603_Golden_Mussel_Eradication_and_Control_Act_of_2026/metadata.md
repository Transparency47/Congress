# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4603?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4603
- Title: Golden Mussel Eradication and Control Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4603
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-30T04:53:26Z
- Update date including text: 2026-05-30T04:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4603",
    "number": "4603",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Golden Mussel Eradication and Control Act of 2026",
    "type": "S",
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
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T19:53:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4603is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4603\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Schiff (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Nonindigenous Aquatic Nuisance Prevention and Control Act of 1990 to establish a demonstration program with respect to the golden mussel.\n#### 1. Short title\nThis Act may be cited as the Golden Mussel Eradication and Control Act of 2026 .\n#### 2. Golden mussel demonstration program\nSection 1202 of the Nonindigenous Aquatic Nuisance Prevention and Control Act of 1990 ( 16 U.S.C. 4722 ) is amended\u2014\n**(1)**\nby redesignating subsections (j) and (k) as subsections (k) and (l), respectively; and\n**(2)**\nby inserting after subsection (i) the following:\n(j) Golden mussel demonstration program (1) Demonstration program (A) In general The Task Force, in partnership with State and local entities, port authorities, industry partners, institutions of higher education, and local nonprofit organizations, shall develop a demonstration program of prevention, monitoring, control, eradication, education, and research with respect to the golden mussel, including\u2014 (i) research and development regarding\u2014 (I) the biology; (II) the environmental tolerances; (III) the effect on\u2014 (aa) fisheries; (bb) water quality; and (cc) other ecosystem components; and (IV) the efficacy of control mechanisms and technologies; (ii) tracking dispersal and establishment of an early warning system to alert likely areas of future infestations; (iii) development of control and eradication methods and plans, including\u2014 (I) in and around\u2014 (aa) derelict vessels; (bb) public infrastructure; (cc) fish screens; and (dd) waterways; and (II) hull inspections; and (iv) provision of technical assistance to regional, State and local entities to carry out this subsection, as applicable. (B) Implementation area The demonstration program shall be implemented in the Sacramento-San Joaquin Delta and any other waters of the United States the Task Force determines are infested, or likely to become infested, by the golden mussel. (C) Availability of certain information The Task Force shall collect and make available to State and local entities and port authorities, through direct reports, publications, and other means necessary, information relating to control and eradication methods and plans developed under the demonstration program. (D) Control and eradication guidelines Not later than 1 year after the date of the enactment of this subsection, the Task Force shall develop guidelines to control the spread of and eradicate the golden mussel, including through the establishment of watercraft inspection stations. (2) Response and containment research grant program (A) In general The Task Force shall establish a grant program to award amounts, on a competitive basis, to State and local entities, institutions of higher education, nonprofit organizations, and industry partners to carry out projects that\u2014 (i) identify effective technologies and mechanisms to control and remove golden mussels from\u2014 (I) water intakes; (II) conveyance infrastructure; (III) fish screens; (IV) derelict vessels; (V) boat hulls; (VI) waterways; or (VII) other areas where the golden mussel may be found; or (ii) provide an understanding of the biology of the golden mussel and effective containment science with respect to the golden mussel. (B) Technology transfer In carrying out the grant program, the Task Force may enter into an agreement with a State or local entity, port authority, industry partner, or any other appropriate entity for the use or sale of any new technology developed under the grant program to expedite the control and eradication of golden mussels. (3) Coordination (A) In general The demonstration program shall provide guidance to other Federal agencies, States, port authorities for all United States ports of entry, local government agencies, and regional and other entities with the necessary expertise to participate in control and eradication methods and plans developed pursuant to the demonstration program. (B) Delegation The Task Force may delegate responsibility for implementing all or a portion of a control or eradication method or plan developed pursuant to the demonstration program to an entity described in subparagraph (A) if the Task Force determines\u2014 (i) such entity has sufficient authority or jurisdiction and expertise; and (ii) it will be more efficient or effective to delegate such responsibility than to retain such responsibility. (4) Authorization of appropriations There are authorized to be appropriated to the Task Force to carry out this section $15,000,000 for each of fiscal years 2026 through 2030. (5) Definitions In this subsection: (A) Demonstration program The term demonstration program means the demonstration program developed under paragraph (1)(A). (B) Grant program The term grant program means the grant program established under paragraph (2)(A). (C) Institution of higher education The term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). .",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4603is.xml"
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
      "title": "Golden Mussel Eradication and Control Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Golden Mussel Eradication and Control Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Nonindigenous Aquatic Nuisance Prevention and Control Act of 1990 to establish a demonstration program with respect to the golden mussel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T04:48:24Z"
    }
  ]
}
```
