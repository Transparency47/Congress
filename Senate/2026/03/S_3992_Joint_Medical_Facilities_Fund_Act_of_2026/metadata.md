# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3992?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3992
- Title: Joint Medical Facilities Fund Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3992
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-05-21T11:03:37Z
- Update date including text: 2026-05-21T11:03:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3992",
    "number": "3992",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Joint Medical Facilities Fund Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T11:03:37Z",
    "updateDateIncludingText": "2026-05-21T11:03:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-04",
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
        "item": [
          {
            "date": "2026-04-29T21:37:32Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-04T22:15:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "AK"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3992is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3992\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Banks (for himself, Ms. Hirono , and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 10, United States Code, to codify authority for the Joint Medical Facility Fund of the Department of Defense and the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Joint Medical Facilities Fund Act of 2026 .\n#### 2. Codification of authority for Joint Medical Facility Fund of Department of Defense and Department of Veterans Affairs\n##### (a) In general\nChapter 55 of title 10, United States Code, is amended by adding at the end the following new section:\n1110c. Joint Medical Facility Fund (a) Establishment There is established on the books of the Treasury under the Department of Veterans Affairs a fund to be known as the Joint Medical Facility Fund (in this section referred to as the Fund ). (b) Purpose The purpose of the Fund shall be to facilitate the joint funding of designated combined Federal medical facilities of the Department of Defense and the Department of Veterans Affairs. (c) Transfers to fund (1) In general Amounts may be transferred to the Fund by the Secretary of Defense from amounts authorized and appropriated for the Department of Defense and by the Secretary of Veterans Affairs from amounts authorized and appropriated for the Department of Veterans Affairs, as determined by a methodology jointly established by the Secretary of Defense and the Secretary of Veterans Affairs that reflects the mission-specific activities, workload, and costs of provision of health care at the facilities of the Department of Defense and the Department of Veterans Affairs, respectively. (2) Transfers of amounts from medical care collections Amounts may be transferred to the Fund from medical care collections under the following authorities for health care provided at designated combined Federal medical facilities of the Department of Defense and the Department of Veterans Affairs: (A) Section 1095 of this title. (B) Section 1729 of title 38. (C) The Act entitled An Act to provide for the recovery from tortiously liable third persons of the cost of hospital and medical care and treatment furnished by the United States ( Public Law 87\u2013693 ; 42 U.S.C. 2651 et seq. ; commonly known as the Federal Medical Care Recovery Act ). (d) Availability of amounts in fund (1) In general Amounts transferred to the Fund under subsection (c) shall be available to fund the operations of designated combined Federal medical facilities of the Department of Defense and the Department of Veterans Affairs, including capital equipment, real property maintenance, and minor construction projects that are not required to be specifically authorized by law under section 2805 of this title or section 8104 of title 38. (2) Captain James A. Lovell Federal Health Care Center Amounts transferred to the Fund by the Secretary of Defense under subsection (c) may be used for facility operations of the Captain James A. Lovell Federal Health Care Center, consisting of the North Chicago Veterans Affairs Medical Center, the Navy Ambulatory Care Center, and supporting facilities designated as a combined Federal medical facility under an operational agreement covered by section 706 of the Duncan Hunter National Defense Authorization Act for Fiscal Year 2009 ( Public Law 110\u2013417 ; 122 Stat. 4500). (3) Limitation The availability of amounts transferred to the Fund under subsection (c)(2) shall be subject to the provisions of section 1729A of title 38. (4) Period of availability (A) In general Except as provided in subparagraph (B), amounts transferred to the Fund under subsection (c) shall remain available under this subsection until the end of the first fiscal year beginning after the date of the transfer. (B) Exception Of the amount transferred to the Fund under subsection (c) in a fiscal year, an amount not to exceed two percent of such amount shall remain available under this subsection until the end of the second fiscal year beginning after the date of the transfer. (e) Executive agreement (1) Fund administration (A) In general The Fund shall be administered in accordance with an executive agreement between the Secretary of Defense and the Secretary of Veterans Affairs. (B) Guidelines The executive agreement under subparagraph (A) shall be consistent with section 706 of the Duncan Hunter National Defense Authorization Act for Fiscal Year 2009 ( Public Law 110\u2013417 ; 122 Stat. 4500) and shall provide for an independent review of the methodology established under subsection (c)(1). (2) Financial reconciliation (A) In general The executive agreement between the Secretary of Defense and the Secretary of Veterans Affairs under paragraph (1)(A) shall provide for the development and implementation of an integrated financial reconciliation process that meets the fiscal reconciliation requirements of the Department of Defense and the Department of Veterans Affairs. (B) Identification of contributions The process under subparagraph (A) shall permit the Department of Defense and the Department of Veterans Affairs to identify their fiscal contributions to the Fund, taking into consideration accounting, workload, and financial management differences. .\n##### (b) Conforming repeal\nSection 1704 of the National Defense Authorization Act for Fiscal Year 2010 ( Public Law 111\u201384 ; 123 Stat. 2571), as most recently amended by section 1421 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ), is repealed.\n##### (c) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense and the Secretary of Veterans Affairs shall jointly submit to the Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the Senate and the Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the House of Representatives a report indicating medical facilities of the Department of Defense or the Department of Veterans Affairs that either Secretary, or both, considers appropriate to be designated as combined Federal medical facilities of the Department of Defense and the Department of Veterans Affairs.",
      "versionDate": "2026-03-04",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-20T15:32:29Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3992is.xml"
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
      "title": "Joint Medical Facilities Fund Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T11:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Joint Medical Facilities Fund Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to codify authority for the Joint Medical Facility Fund of the Department of Defense and the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:49Z"
    }
  ]
}
```
