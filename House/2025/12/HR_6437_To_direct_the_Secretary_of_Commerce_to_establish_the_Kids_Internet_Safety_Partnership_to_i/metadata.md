# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6437
- Title: Kids Internet Safety Partnership Act
- Congress: 119
- Bill type: HR
- Bill number: 6437
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-04-28T13:40:07Z
- Update date including text: 2026-04-28T13:40:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-04 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-04 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6437",
    "number": "6437",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "F000478",
        "district": "7",
        "firstName": "Russell",
        "fullName": "Rep. Fry, Russell [R-SC-7]",
        "lastName": "Fry",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Kids Internet Safety Partnership Act",
    "type": "HR",
    "updateDate": "2026-04-28T13:40:07Z",
    "updateDateIncludingText": "2026-04-28T13:40:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:30:47Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:30:36Z",
                "name": "Markup by"
              },
              {
                "date": "2025-12-04T21:30:21Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "OH"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6437ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6437\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Fry (for himself and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Commerce to establish the Kids Internet Safety Partnership to identify and advance best practices with respect to the online safety of minors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kids Internet Safety Partnership Act .\n#### 2. Kids Internet Safety Partnership\n##### (a) Establishment\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall establish the Kids Internet Safety Partnership.\n##### (b) Director\nThe Secretary shall appoint a Director to be the head of the Partnership.\n##### (c) Duties\nThe duties of the Partnership shall be the following:\n**(1)**\nCoordinate with relevant Federal agencies, including the Federal Trade Commission, and stakeholders to identify\u2014\n**(A)**\nthe risks for minors with respect to the use of websites, online services, online applications, and mobile applications;\n**(B)**\nthe benefits for minors with respect to the use of websites, online services, online applications, and mobile applications; and\n**(C)**\nwidely accepted or evidence-based best practices that account for minors of different ages and\u2014\n**(i)**\naddress the risks identified under subparagraph (A); and\n**(ii)**\npreserve and enhance the benefits identified under subparagraph (B).\n**(2)**\nNot later than 1 year after the date on which the Partnership is established, and every 2 years thereafter, publish on a publicly available website a report that details\u2014\n**(A)**\nthe identifications made under paragraph (1); and\n**(B)**\nthe efficacy and adoption by websites, online services, online applications, and mobile applications of\u2014\n**(i)**\nsafeguards for minors; and\n**(ii)**\nparental tools.\n**(3)**\nNot later than 2 years after the date on which the Partnership is established, publish on a publicly available website a playbook for providers and developers of websites, online services, online applications, and mobile applications to facilitate the implementation of widely accepted or evidence-based best practices that account for minors of different ages and address the risks identified under paragraph (1)(A) and preserve and enhance the benefits identified under paragraph (1)(B), including best practices with respect to\u2014\n**(A)**\nage verification, assurance, and estimation techniques;\n**(B)**\ndesign features;\n**(C)**\nparental tools;\n**(D)**\ndefault privacy and account settings;\n**(E)**\nreporting systems and tools;\n**(F)**\nthird-party safety software services; and\n**(G)**\nlimitations and opt-outs related to personalized recommendation systems and chatbots.\n##### (d) Stakeholders\nIn coordinating with stakeholders under subsection (c)(1), the Partnership shall coordinate with the following:\n**(1)**\nAcademic experts with specific expertise with respect to the prevention of risks for minors online.\n**(2)**\nResearchers with specific expertise with respect to social media.\n**(3)**\nParents and minors with demonstrated experience with respect to the safety of minors online.\n**(4)**\nEducators with demonstrated experience with respect to the safety of minors online.\n**(5)**\nOnline platforms.\n**(6)**\nExperts in academia and civil society with specific expertise with respect to constitutional law, privacy, free expression, access to information, and civil liberties.\n**(7)**\nState attorneys general (or designees thereof who work in State or local government).\n##### (e) Sunset\nThe Partnership shall terminate on the date that is 5 years after the date on which the Partnership is established.\n##### (f) Definitions\nIn this section:\n**(1) Design feature**\nThe term design feature \u2014\n**(A)**\nmeans any feature or component of a website, online service, online application, or mobile application that encourages an increase in or increases the frequency of use or time spent by a user who is a minor with respect to such website, service, or application; and\n**(B)**\nincludes\u2014\n**(i)**\ninfinite scrolling or auto play;\n**(ii)**\nrewards or incentives based on frequency of use or time spent;\n**(iii)**\nnotifications and push alerts;\n**(iv)**\nbadges or other visual award symbols based on frequency of use or time spent; and\n**(v)**\nappearance altering filters.\n**(2) Minor**\nThe term minor means an individual who is under the age of 18.\n**(3) Parent**\nThe term parent means a legal guardian of a minor.\n**(4) Parental tool**\nThe term parental tool \u2014\n**(A)**\nmeans a tool that\u2014\n**(i)**\na website, online service, online application, or mobile application provides to a parent of a user who the service or application knows is a minor; and\n**(ii)**\nthe parent uses to support such user with respect to the use of the website, service, or application; and\n**(B)**\nincludes a tool that allows a parent of a user who the website, service, or application knows is a minor to\u2014\n**(i)**\nview or change the privacy and account settings of such user;\n**(ii)**\ngrant or withdraw verifiable parental consent;\n**(iii)**\nrestrict the purchases and financial transactions of such user;\n**(iv)**\nview metrics of the total time spent on such website, service, or application by such user;\n**(v)**\nrestrict time spent on such website, service, or application by such user;\n**(vi)**\nreport illegal or harmful conduct on such website, service, or application with respect to which such user may be a victim; and\n**(vii)**\nlimit or opt-out of personalized recommendation systems or chatbots.\n**(5) Partnership**\nThe term Partnership means the Kids Internet Safety Partnership established under subsection (a).\n**(6) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(7) Verifiable parental consent**\nThe term verifiable parental consent has the meaning given such term in section 1302 of the Children's Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ).",
      "versionDate": "2025-12-04",
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
        "actionDate": "2026-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7757",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "KIDS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2026-01-07T18:37:30Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-01-07T18:30:19Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-01-07T18:35:30Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-07T18:30:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-10T21:35:42Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6437ih.xml"
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
      "title": "Kids Internet Safety Partnership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kids Internet Safety Partnership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Commerce to establish the Kids Internet Safety Partnership to identify and advance best practices with respect to the online safety of minors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:18Z"
    }
  ]
}
```
