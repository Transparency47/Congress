# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8733?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8733
- Title: Melanie's Law
- Congress: 119
- Bill type: HR
- Bill number: 8733
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-22T10:23:36Z
- Update date including text: 2026-05-22T10:23:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8733",
    "number": "8733",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Melanie's Law",
    "type": "HR",
    "updateDate": "2026-05-22T10:23:36Z",
    "updateDateIncludingText": "2026-05-22T10:23:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
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
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
          "date": "2026-05-11T14:31:45Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8733ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8733\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Ryan introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program to support protective orders that protect individuals who are related by blood or marriage to individuals in intimate relationships, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Melanie's Law .\n#### 2. Grant program to support protective orders that protect individuals who are related by blood or marriage to individuals in intimate relationships\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP MELANIE\u2019S LAW: GRANT PROGRAM TO SUPPORT PROTECTIVE ORDERS THAT PROTECT INDIVIDUALS RELATED BY BLOOD OR MARRIAGE TO INDIVIDUALS IN INTIMATE RELATIONSHIPS 3061. Purpose; definition of Melanie\u2019s Law protective order authorities (a) Purpose The purpose of this part is to support States to implement the Melanie\u2019s Law protective order authorities and carry out related activities involving protective orders and domestic violence. (b) Definition of Melanie\u2019s Law protective order authorities In this part, the term Melanie\u2019s Law protective order authorities means laws that ensure that family courts and criminal courts, as applicable, have each of the following authorities: (1) The jurisdiction and authority to issue and enforce a protective order that protects one individual from another, where the two individuals\u2014 (A) are related by consanguinity or affinity; (B) are legally married to each other; (C) were formerly married to each other, regardless of whether the individuals still reside in the same household; (D) have a child in common, regardless of whether the individuals have been married or have lived together at any time; or (E) are or have been in an intimate relationship with each other. (2) In a situation in which two individuals are or have been in an intimate relationship with each other, the jurisdiction and authority to issue and enforce a protective order that protects a third individual, regardless of age, where that third individual is related by consanguinity or affinity to either of the two individuals. 3062. Grants (a) Authority The Attorney General may make grants to eligible States for the following purposes: (1) To provide education and training to law enforcement officers, prosecutors, and courts on the Melanie\u2019s Law protective order authorities and the implementation of those authorities. (2) To facilitate the service of process of protective orders, such as by enabling or improving service of process\u2014 (A) in person or by electronic means; or (B) across State, Tribal, or local jurisdictional lines. (3) To establish or enhance\u2014 (A) systems that manage and track information about protective orders and violations of protective orders, such as systems operated by law enforcement agencies or courts; and (B) mechanisms for the sharing of such information between and among such systems. (4) To support official units or positions that have specialized responsibilities with respect to protective orders or domestic violence, such as to enforce or promote compliance, to prosecute violations, or to coordinate with others on such matters. (5) To enable or improve the provision to victims in matters involving protective orders of\u2014 (A) civil legal services, to help such victims obtain, modify, and enforce protective orders or to represent such victims in related matters involving immigration or custody; (B) victim advocacy services, hotline services, and crisis response services; (C) emergency shelter services, relocation assistance, transportation assistance, childcare assistance, and short-term housing assistance; (D) access to counseling, trauma-informed therapy, and case management; and (E) access to communications equipment and services for personal safety and for participation in hearings or other official proceedings. (b) Eligibility To be eligible for grants under this section, a State must have in effect, and must certify that it has in effect, the Melanie\u2019s Law protective order authorities. (c) Use of grant amounts Upon request of an eligible State, the Attorney General may permit the State to use grant amounts under this part to provide the non-Federal share of the cost of programs or projects funded by other grant programs administered by the Attorney General that provide support or services to victims. 3063. Applications (a) In general To request a grant under this part, the chief executive of a State shall submit an application to the Attorney General in such form and containing such information as the Attorney General may reasonably require. Such application shall include assurances that Federal funds received under this part shall be used to supplement, not supplant, non-Federal funds that would otherwise be available for activities funded under this part, except as provided in section 3062(c). (b) Implementation plan Such application shall include an implementation plan describing how the funds will be used, what performance measures will be applied, and how the State will coordinate and partner with the relevant elements of the justice system, judicial system, and victims services system. 3064. Allocations (a) In general For each fiscal year, of the amounts authorized to be appropriated for that fiscal year, the Attorney General may obligate\u2014 (1) not more than 75 percent for grants to eligible States on a formula basis, with each such State receiving an amount that bears the same ratio to the 75 percent as the population of the State bears to the population of all such States; (2) not more than 22 percent for grants to eligible States on a competitive basis; and (3) not more than 3 percent for the administrative expenses of the Attorney General in carrying out this part for that fiscal year, including technical assistance, training, evaluation, and program administration. (b) Minimum allocation under formula Notwithstanding subsection (a)(1), each eligible State shall receive an amount under subsection (a)(1) of not less than 0.5 percent. 3065. Reports Each grantee receiving funds under this part shall submit a report to the Attorney General evaluating the effectiveness of projects developed with funds provided under this part and containing such additional information as the Attorney General may prescribe. 3066. Definition of State In this part, the term State means each of the several States and the District of Columbia, the Commonwealth of Puerto Rico, Guam, American Samoa, the Virgin Islands, and the Northern Mariana Islands. 3067. Authorization of appropriations There are authorized to be appropriated to carry out this part $200,000,000 for each of fiscal years 2026 through 2036. .",
      "versionDate": "2026-05-11",
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8733ih.xml"
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
      "title": "Melanie's Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Melanie's Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T10:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program to support protective orders that protect individuals who are related by blood or marriage to individuals in intimate relationships, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:32Z"
    }
  ]
}
```
