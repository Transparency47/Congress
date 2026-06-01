# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8033
- Title: No Harm Data Centers Act
- Congress: 119
- Bill type: HR
- Bill number: 8033
- Origin chamber: House
- Introduced date: 2026-03-20
- Update date: 2026-03-27T20:09:47Z
- Update date including text: 2026-03-27T20:09:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-20: Introduced in House
- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-20: Introduced in House

## Actions

- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Introduced in House
- 2026-03-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-20",
    "latestAction": {
      "actionDate": "2026-03-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8033",
    "number": "8033",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000601",
        "district": "1",
        "firstName": "Greg",
        "fullName": "Rep. Landsman, Greg [D-OH-1]",
        "lastName": "Landsman",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "No Harm Data Centers Act",
    "type": "HR",
    "updateDate": "2026-03-27T20:09:47Z",
    "updateDateIncludingText": "2026-03-27T20:09:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-20",
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
      "actionDate": "2026-03-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-20",
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
          "date": "2026-03-20T14:30:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8033ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8033\nIN THE HOUSE OF REPRESENTATIVES\nMarch 20, 2026 Mr. Landsman introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure that American families are protected from the impacts of data centers on the electric grid, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Harm Data Centers Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\ndata centers, while creating potentially economically valuable tools, impose costs upon other electricity customers, in the form of higher costs for the generation of electricity, along with necessary investments in electric infrastructure; and\n**(2)**\nthe costs imposed by data centers upon the bulk-power system should be fully borne by data centers and that other residential and small commercial electricity customers should be economically protected from the impacts of data centers.\n#### 3. Ensuring data centers pay their fair share\n##### (a) Data center defined\nSection 3 of the Federal Power Act ( 16 U.S.C. 796 ) is amended by adding at the end the following:\n(30) Data center The term data center means\u2014 (A) any facility that\u2014 (i) is behind a single point of interconnection; (ii) primarily contains electronic equipment used to process, store, and transmit digital information; and (iii) has a peak electricity demand of greater than 50 megawatts; or (B) any group of facilities\u2014 (i) that are behind a single point of interconnection; (ii) the majority of which primarily contain electronic equipment used to process, store, and transmit digital information; and (iii) that, in the aggregate, have a peak electricity demand of greater than 50 megawatts. .\n##### (b) Ensuring data centers pay their fair share\nThe Federal Power Act is amended by inserting after section 223 ( 16 U.S.C. 824w ) the following:\n224. Ensuring data centers pay their fair share (a) Authority (1) In general Notwithstanding subsection (a) and subsection (b)(1) of section 201, and subject to subsection (d), the Commission shall, beginning on the date that is 90 days after the date of enactment of this section, have the sole authority to approve rates and charges for the retail sale of electric energy from a covered electric utility to a data center. (2) Just and reasonable requirement All rates and charges approved by the Commission pursuant to paragraph (1) shall be just and reasonable, and not unduly discriminatory or preferential. If the Commission finds, after a hearing held upon its own motion or upon complaint, that any rate or charge approved by the Commission is unjust or unreasonable, or unduly discriminatory or preferential, the Commission shall fix a new rate or charge that is just and reasonable and not unduly discriminatory or preferential. (b) Full allocation of costs Any rate or charge approved pursuant to subsection (a) shall include\u2014 (1) the full costs of constructing, upgrading, and expanding any transmission or distribution facility to facilitate the interconnection of data centers to the bulk-power system; (2) the full costs of constructing, upgrading, and expanding any transmission or distribution facility to ensure the reliability of the bulk-power system during periods of increasing demand for electric energy from data centers; and (3) the full costs of constructing, upgrading, and expanding any generating facility to facilitate the reliability of the bulk-power system during periods of increasing demand for electric energy from data centers. (c) Prohibition on cost-shifting No covered electric utility may shift the costs described in paragraphs (1) through (3) of subsection (b) onto their retail rates or charges for any customer other than a data center. (d) Inapplicability This section shall not apply within the area referred to in section 212(k)(2)(A). (e) Definitions In this section: (1) Commission The term Commission means the Federal Energy Regulatory Commission. (2) Covered electric utility The term covered electric utility means a person that sells electric energy, except\u2014 (A) an electric cooperative described in section 201(f); (B) an electric utility that is owned or operated by a State or political subdivision thereof; (C) the Tennessee Valley Authority; and (D) each Federal power marketing administration. .\n##### (c) Penalties\nThe Federal Power Act ( 16 U.S.C. 792 et seq. ) is amended\u2014\n**(1)**\nin section 221, by inserting , the price of electricity sold to data centers at retail and inputs to such price, after sold at wholesale ;\n**(2)**\nin section 307(a), by inserting , the sale of electric energy at retail to data centers, after at wholesale in interstate commerce ;\n**(3)**\nin section 311, by striking and industrial and inserting data center, and industrial ; and\n**(4)**\nin section 316A(b)\u2014\n**(A)**\nby striking Any person who violates any provision of part II and inserting the following:\n(1) In general Any person who violates any provision of part II, except for section 224, ;\n**(B)**\nby striking Such penalty and inserting the following:\n(2) Data center violations Any person who violates any provision of section 224 or any provision of any rule or order thereunder shall be subject to a civil penalty of not more than $10,000,000 for each day that such violation continues. (3) Assessment A penalty under this subsection ; and\n**(C)**\nby striking In determining the amount of a proposed penalty, and inserting the following:\n(4) Penalty amount In determining the amount of a proposed penalty under this subsection, .\n##### (d) Conforming amendment\nSection 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) ) is amended by striking or 222 and inserting 222, or 224 .\n#### 4. Limitation on judicial enforceability of predispute nondisclosure contract clauses relating to the construction of data centers\n##### (a) In general\n**(1) Enforceability against public officials**\nWith respect to the construction of a data center, no predispute nondisclosure clause shall be judicially enforceable against a public official.\n**(2) Continued applicability of state law**\nThis section shall not be construed to supersede a provision of State law that establishes, implements, or continues in effect a requirement or prohibition except to the extent that such requirement or prohibition prevents the application of this section.\n##### (b) Applicability\nThis section shall apply with respect to a claim that is filed under Federal, State, or Tribal law on or after the date of the enactment of this Act.\n#### 5. Assessment of environmental and public health effects of data centers\nThe Administrator of the Environmental Protection Agency shall seek to enter into an agreement with the National Academies under which the National Academies shall\u2014\n**(1)**\nconduct an assessment of the impacts of data centers on the environment and public health, including with respect to\u2014\n**(A)**\nnoise pollution;\n**(B)**\nair pollution;\n**(C)**\nwater consumption;\n**(D)**\nwater supply;\n**(E)**\ncarbon emissions; and\n**(F)**\nwaste, including electronic waste;\n**(2)**\ndevelop recommendations to mitigate such impacts; and\n**(3)**\nnot later than 180 days after the date of the enactment of this Act, submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Environment and Public Works of the Senate a report containing the results of the assessment conducted under paragraph (1) and the recommendations developed under paragraph (2).\n#### 6. Definitions\nFor purposes of this Act:\n**(1) Data center**\nThe term data center means\u2014\n**(A)**\nany facility that\u2014\n**(i)**\nis behind a single point of interconnection;\n**(ii)**\nprimarily contains electronic equipment used to process, store, and transmit digital information; and\n**(iii)**\nhas a peak electricity demand of greater than 50 megawatts; or\n**(B)**\nany group of facilities\u2014\n**(i)**\nthat are behind a single point of interconnection;\n**(ii)**\nthe majority of which primarily contain electronic equipment used to process, store, and transmit digital information; and\n**(iii)**\nthat, in the aggregate, have a peak electricity demand of greater than 50 megawatts.\n**(2) National Academies**\nThe term National Academies means the National Academies of Sciences, Engineering, and Medicine.\n**(3) Predispute nondisclosure clause**\nThe term predispute nondisclosure clause means a provision in a contract or agreement agreed to before a lawsuit is filed under Federal, State, or Tribal law, that requires the parties to the contract or agreement not to disclose or discuss conduct, the existence of a settlement involving conduct, or information covered by the terms and conditions of the contract or agreement.\n**(4) Public official**\nThe term public official means an individual who, at the time a contract or agreement was agreed to, was an elected official of a Federal, State, or local unit of government in the United States.",
      "versionDate": "2026-03-20",
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
        "name": "Energy",
        "updateDate": "2026-03-27T20:09:47Z"
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
      "date": "2026-03-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8033ih.xml"
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
      "title": "No Harm Data Centers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Harm Data Centers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that American families are protected from the impacts of data centers on the electric grid, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T08:18:36Z"
    }
  ]
}
```
