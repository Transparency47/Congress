# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/799
- Title: Parental Notification and Intervention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 799
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-04-17T16:05:48Z
- Update date including text: 2025-04-17T16:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/799",
    "number": "799",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Parental Notification and Intervention Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-17T16:05:48Z",
    "updateDateIncludingText": "2025-04-17T16:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:09:40Z",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "AL"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WV"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr799ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 799\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Miller of Illinois (for herself, Mr. Babin , Mr. Finstad , Mr. Moore of Alabama , Mr. Moore of West Virginia , Mr. Ogles , Mr. Webster of Florida , Ms. Tenney , Mr. Harris of Maryland , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for parental notification and intervention in the case of an unemancipated minor seeking an abortion.\n#### 1. Short title\nThis Act may be cited as the Parental Notification and Intervention Act of 2025 .\n#### 2. Parental notification\n##### (a) In general\nIt shall be unlawful for any person or organization in or affecting interstate or foreign commerce or who solicits or accepts Federal funds to perform any abortion on an unemancipated minor under the age of 18, to permit the facilities of the person or organization to be used to perform any abortion on such a minor, or to assist in the performance of any abortion on such a minor if the person or organization has failed to comply with all of the following requirements:\n**(1)**\nThe provision of written notification to the parents (as defined in subsection (e)) of the minor informing the parents that an abortion has been requested for the minor, except that such notification is not required for a parent if the physician is presented with documentation showing with a reasonable degree of certainty that a court of record in the minor's State of residence has waived any parental notification. The court of record shall not waive any parental notification requirement unless there is clear and convincing evidence of physical abuse of the minor by such parent.\n**(2)**\nCompliance with a 96-hour waiting period after notice has been received by the parents.\n**(3)**\nCompliance with any injunction granted under section 3 relating to the abortion.\n##### (b) Fine for violation\nWhoever willfully violates subsection (a) shall be fined not more than $100,000 or imprisoned not more than one year, or both, for each violation.\n##### (c) Exception\nSubsection (a) shall not apply with respect to an unemancipated minor for whom an abortion is sought if a physician (other than the physician with principal responsibility for making the decision to perform the abortion) makes a determination that\u2014\n**(1)**\na medical emergency exists which, with reasonable medical certainty, so complicates the medical condition of the minor that the death of the minor would result from the failure to immediately treat her physical condition even though the treatment may result in the death of her unborn child;\n**(2)**\nparental notification is not possible as a result of the medical emergency; and\n**(3)**\ncertifications regarding compliance with paragraphs (1) and (2) have been entered in the medical records of the minor, together with the reasons upon which the determinations are based, including a statement of relevant clinical findings.\n##### (d) Parental notification requirements\nFor purposes of this section, any parental notification provided to comply with the provisions of subsection (a) for a parent shall be\u2014\n**(1)**\ndelivered personally to the parent; or\n**(2)**\nprovided through certified mail in accordance with all of the following procedures:\n**(A)**\nThe certified mail is addressed to the parent.\n**(B)**\nThe address used is the dwelling or usual place of abode of the parent.\n**(C)**\nA return receipt is requested.\n**(D)**\nThe delivery is restricted to the parent.\n##### (e) Parent defined To include legal guardian\nFor purposes of this Act, the term parent includes, with respect to an unemancipated minor, any legal guardian of the minor.\n#### 3. Parental intervention\nAny parent required to be notified pursuant to section 2 regarding an abortion of an unemancipated minor may bring an action in the Federal district court where the parent resides or where the unemancipated minor is located to enjoin the performance of the abortion. The court shall issue a temporary injunction barring the performance of the abortion until the issue has been adjudicated and the judgment is final. The court shall issue relief permanently enjoining the abortion unless the court determines that granting such relief would be unlawful.\n#### 4. Preemption\nNothing in this Act shall be construed to preempt any provision of State law to the extent that such State law establishes, implements, or continues in effect greater parental notification requirements or intervention rights regarding abortion than those provided under this Act.\n#### 5. Effective date and severability\n##### (a) Effective date\nThe provisions of this Act shall take effect upon its enactment.\n##### (b) Severability\nThe provisions of this Act shall be severable. If any provision of this Act, or any application thereof, is found unconstitutional, that finding shall not affect any provision or application of the Act not so adjudicated.",
      "versionDate": "2025-01-28",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-04-01T15:14:20Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-01T15:14:20Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-04-01T15:14:20Z"
          },
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2025-04-01T15:14:20Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-04-01T15:14:20Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-01T15:14:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-01T15:32:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr799",
          "measure-number": "799",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr799v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong><strong>Parental Notification and Intervention Act of 2025</strong></strong></p><p>This bill restricts the performance of an abortion on an unemancipated minor under 18 years of age.</p><p>Specifically, it prohibits a person or organization from performing, facilitating, or assisting with an abortion on an unemancipated minor without first complying with certain requirements, including parental notification and a 96-hour waiting period.</p><p>It establishes penalties\u2014a fine, up to one year in prison, or both\u2014for each willful violation.</p><p>A parent who is required to be notified of an abortion of an unemancipated minor may sue in federal court to prohibit the abortion.</p><p>Parental notification requirements may be waived in a medical emergency or in a case of physical abuse.</p>"
        },
        "title": "Parental Notification and Intervention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr799.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong><strong>Parental Notification and Intervention Act of 2025</strong></strong></p><p>This bill restricts the performance of an abortion on an unemancipated minor under 18 years of age.</p><p>Specifically, it prohibits a person or organization from performing, facilitating, or assisting with an abortion on an unemancipated minor without first complying with certain requirements, including parental notification and a 96-hour waiting period.</p><p>It establishes penalties\u2014a fine, up to one year in prison, or both\u2014for each willful violation.</p><p>A parent who is required to be notified of an abortion of an unemancipated minor may sue in federal court to prohibit the abortion.</p><p>Parental notification requirements may be waived in a medical emergency or in a case of physical abuse.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr799"
    },
    "title": "Parental Notification and Intervention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong><strong>Parental Notification and Intervention Act of 2025</strong></strong></p><p>This bill restricts the performance of an abortion on an unemancipated minor under 18 years of age.</p><p>Specifically, it prohibits a person or organization from performing, facilitating, or assisting with an abortion on an unemancipated minor without first complying with certain requirements, including parental notification and a 96-hour waiting period.</p><p>It establishes penalties\u2014a fine, up to one year in prison, or both\u2014for each willful violation.</p><p>A parent who is required to be notified of an abortion of an unemancipated minor may sue in federal court to prohibit the abortion.</p><p>Parental notification requirements may be waived in a medical emergency or in a case of physical abuse.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr799"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr799ih.xml"
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
      "title": "Parental Notification and Intervention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parental Notification and Intervention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for parental notification and intervention in the case of an unemancipated minor seeking an abortion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:24Z"
    }
  ]
}
```
