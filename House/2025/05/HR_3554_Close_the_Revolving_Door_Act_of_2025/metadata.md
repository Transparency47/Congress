# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3554
- Title: Close the Revolving Door Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3554
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-12-05T21:34:31Z
- Update date including text: 2025-12-05T21:34:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3554",
    "number": "3554",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Close the Revolving Door Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:34:31Z",
    "updateDateIncludingText": "2025-12-05T21:34:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:03:45Z",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MN"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MI"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3554ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3554\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Neguse introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide greater controls and restrictions on revolving door lobbying.\n#### 1. Short title\nThis Act may be cited as the Close the Revolving Door Act of 2025 .\n#### 2. Lifetime ban on Members of Congress from lobbying\n##### (a) In general\nSection 207(e)(1) of title 18, United States Code, is amended to read as follows:\n(1) Members of Congress Any person who is a Senator, a Member of the House of Representatives, or an elected officer of the Senate or the House of Representatives and who, after that person leaves office, knowingly makes, with the intent to influence, any communication to or appearance before any Member, officer, or employee of either House of Congress or any employee of any other legislative office of the Congress, on behalf of any other person (except the United States) in connection with any matter on which such former Senator, Member, or elected official seeks action by a Member, officer, or employee of either House of Congress, in his or her official capacity, shall be punished as provided in section 216 of this title. .\n##### (b) Conforming amendments\nSection 207(e)(2) of title 18, United States Code, is amended\u2014\n**(1)**\nin the heading, by striking Officers and staff and inserting Staff ;\n**(2)**\nby striking an elected officer of the Senate, or ;\n**(3)**\nby striking leaves office or employment and inserting leaves employment ; and\n**(4)**\nby striking former elected officer or .\n#### 3. Congressional staff\nParagraphs (2), (3)(A), (4), (5)(A), and (6)(A) of section 207(e) of title 18, United States Code, are each amended by striking 1 year and inserting 6 years .\n#### 4. Improved reporting of lobbyists\u2019 activities\nSection 6 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1605 ) is amended by adding at the end the following:\n(c) Joint website (1) In general The Secretary of the Senate and the Clerk of the House of Representatives shall maintain a joint lobbyist disclosure internet database for information required to be publicly disclosed under this Act which shall be an easily searchable website called lobbyists.gov with a stated goal of simplicity of usage. (2) Authorization of appropriations There is authorized to be appropriated to carry out this subsection $100,000 for fiscal year 2026. .\n#### 5. Lobbyist revolving door to Congress\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term foreign principal has the meaning given that term under section 1(b) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611(b) );\n**(2)**\nthe terms lobbyist and lobbying contact have the meanings given such terms under section 3 of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602 ); and\n**(3)**\nthe term registered lobbyist means a lobbyist registered under the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1601 et seq. ).\n##### (b) Prohibition\nAny person who is a registered lobbyist or an agent of a foreign principal may not, within 6 years after that person leaves such position, be hired by a Member or committee of either House of Congress with whom the registered lobbyist or agent of a foreign principal has had substantial lobbying contact.\n##### (c) Waiver\nThis section may be waived in the Senate or the House of Representatives by the Select Committee on Ethics of the Senate or the Committee on Standards of Official Conduct of the House of Representatives, respectively, based on a compelling national need.\n##### (d) Substantial lobbying contact\nFor purposes of this section, in determining whether a registered lobbyist or agent of a foreign principal has had substantial lobbying contact within the applicable period of time, a Member or committee of either House of Congress shall take into consideration whether the individual's lobbying contacts have pertained to pending legislative business, or related to solicitation of an earmark or other Federal funding, particularly if such contacts included the coordination of meetings with the Member or committee, involved presentations to employees of the Member or committee, or participation in fundraising (except for the mere giving of a personal contribution). Simple social contacts with the Member or committee of either House of Congress and staff, shall not by themselves constitute substantial lobbying contacts.\n#### 6. Reporting by substantial lobbying entities\nThe Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1601 et seq. ) is amended by inserting after section 6 the following:\n6A. Reporting by substantial lobbying entities (a) In general A substantial lobbying entity shall file on an annual basis with the Clerk of the House of Representatives and the Secretary of the Senate a list of each employee of, individual under contract with, or individual who provides paid consulting services to the substantial lobbying entity who is\u2014 (1) a former Senator or a former Member of the House of Representatives; or (2) another covered legislative branch official who\u2014 (A) was paid not less than $100,000 in any 1 year as a covered legislative branch official; (B) worked for a total of not less than 4 years as a covered legislative branch official; or (C) had a job title at any time while employed as a covered legislative branch official that contained any of the following terms: Chief of Staff , Legislative Director , Staff Director , Counsel , Professional Staff Member , Communications Director , or Press Secretary . (b) Contents of filing The filing required under this section shall contain a brief job description of each individual described in subsection (a) and an explanation of their work experience under subsection (a) that requires this filing. (c) Improved reporting of substantial lobbying entities The joint website being maintained by the Secretary of the Senate and the Clerk of the House of Representatives, known as lobbyists.gov, shall include an easily searchable, sortable, and downloadable database with an Application Programming Interface (API) or similar feature entitled Substantial Lobbying Entities that includes information on all individuals described in subsection (a). (d) Law enforcement oversight The Clerk of the House of Representatives and the Secretary of the Senate shall provide a copy of each filing under subsection (a) to the United States Attorney for the District of Columbia, to allow the United States Attorney for the District of Columbia to determine whether a substantial lobbying entity is underreporting the lobbying activities of its employees, individuals under contract, or individuals who provide paid consulting services. (e) Substantial lobbying entity In this section, the term substantial lobbying entity means an incorporated entity that employs more than 3 registered lobbyists during a filing period. .\n#### 7. Enhanced penalties\nSection 7(a) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1606(a) ) is amended, in the matter following paragraph (2), by striking $200,000 and inserting $500,000 .",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-21",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1850",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Close the Revolving Door Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-23T18:28:13Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3554ih.xml"
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
      "title": "Close the Revolving Door Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Close the Revolving Door Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide greater controls and restrictions on revolving door lobbying.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:34Z"
    }
  ]
}
```
