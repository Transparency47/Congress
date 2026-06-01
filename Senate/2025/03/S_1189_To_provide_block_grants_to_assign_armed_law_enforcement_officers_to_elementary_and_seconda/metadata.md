# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1189
- Title: School Guardian Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1189
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-05-01T13:15:59Z
- Update date including text: 2025-05-01T13:15:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1189",
    "number": "1189",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "School Guardian Act of 2025",
    "type": "S",
    "updateDate": "2025-05-01T13:15:59Z",
    "updateDateIncludingText": "2025-05-01T13:15:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T19:28:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1189is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1189\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide block grants to assign armed law enforcement officers to elementary and secondary schools.\n#### 1. Short title\nThis Act may be cited as the School Guardian Act of 2025 .\n#### 2. School guardian grants\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP School guardian grants 3061. Grants for law enforcement officers at schools (a) Definitions In this section\u2014 (1) the term K\u201312 school means an elementary school or secondary school, as such terms are defined under section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ); and (2) the term local educational agency has the meaning given such term under section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (b) Grant authorization Subject to the availability of appropriations, the Attorney General shall make a grant to each State that elects to receive a grant under this section for the cost of assigning armed law enforcement officers to provide security at K\u201312 schools, which may be used for the cost of pay, training, and equipment for the law enforcement officers. (c) Amount A grant under this section to a State for a fiscal year shall be in an amount that bears the same ratio to the total amount awarded under this section for the fiscal year as the total number of individuals attending a K\u201312 school in the State bears to the total number of individuals attending a K\u201312 school in the United States. (d) Administration of grants The use of, and award of subgrants using, amounts received under this section shall be administered by the head of the chief law enforcement agency of a State. (e) Subgrants (1) In general The head of the chief law enforcement agency of a State may award a subgrant to a law enforcement agency of a unit of local government in the State for the cost of hiring 1 or more full-time law enforcement officers who will be assigned to provide full-time security at K\u201312 schools. (2) Agreements (A) In general A law enforcement agency of a unit of local government desiring a subgrant under this subsection shall enter into a written agreement with each K\u201312 school in the jurisdiction of the agency, or with the local educational agency that serves such K\u201312 school, which shall indicate the number of law enforcement officers the law enforcement agency will hire and assign to each such K\u201312 school if awarded a subgrant. (B) Officers at each school The written agreements entered into by a law enforcement agency under subparagraph (A) shall provide for the hiring of not less than 1 full-time law enforcement officer who will be assigned to provide full-time security at each K\u201312 school in the jurisdiction of the law enforcement agency. (3) Amount The amount of a subgrant under this subsection to a law enforcement agency of a unit of local government shall be based on the number of law enforcement officers the law enforcement agency will hire, as indicated in the written agreements described in paragraph (2). (f) Reporting Each State that receives a grant under this section for a fiscal year shall submit to the Attorney General a report regarding the use of the grant for that fiscal year, which shall include\u2014 (1) the number of subgrants awarded; (2) the amount of each subgrant awarded; (3) the number of law enforcement officers hired to provide security at a K\u201312 school using amounts received under the grant; and (4) the number of K\u201312 schools in the State with 1 or more full-time law enforcement officers for whom the cost of the pay, training, or equipment for the law enforcement officers was paid using amounts received under the grant. (g) Failure To use amounts (1) Return A State shall return to the Attorney General any amounts received under a grant under this section for a fiscal year which are unobligated as of the day after the last day of the fiscal year. (2) Use Amounts returned to the Attorney General under paragraph (1) shall be merged with other amounts available to carry out this section and remain available until expended to the Attorney General to make grants under this section, without further appropriation. (3) Reporting The Attorney General shall submit to Congress a report that provides, for each fiscal year, the total amount of funds provided for that fiscal year that are returned under paragraph (1) and the amount of funds provided for that fiscal year that are returned under paragraph (1) by each State. (h) Funding (1) In general Effective on the date of enactment of this Act, of the unobligated balances of amounts made available to the Internal Revenue Service under Public Law 117\u2013169 (136 Stat. 1818), $80,000,000,000 shall be transferred, on a pro rata basis, to the Attorney General to carry out this section. (2) Availability and use Amounts transferred under paragraph (1) shall be merged with, and subject to the same terms and conditions as, other amounts available to carry out this section, and shall remain available until expended. (3) Annual availability of amounts From amounts transferred under paragraph (1), the Attorney General may make not more than $8,000,000,000 in grants under this section for each of fiscal years 2025 through 2034. .",
      "versionDate": "2025-03-27",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-01T13:15:59Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1189is.xml"
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
      "title": "School Guardian Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "School Guardian Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide block grants to assign armed law enforcement officers to elementary and secondary schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:18Z"
    }
  ]
}
```
