# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3739?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3739
- Title: Veterans Hearing Aid Improvement Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3739
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-04-15T11:03:26Z
- Update date including text: 2026-04-15T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3739",
    "number": "3739",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Veterans Hearing Aid Improvement Act of 2026",
    "type": "S",
    "updateDate": "2026-04-15T11:03:26Z",
    "updateDateIncludingText": "2026-04-15T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T19:29:02Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "CA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "IA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3739is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3739\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mrs. Blackburn (for herself, Mr. Schiff , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a demonstration project on coverage by the Department of Veterans Affairs of over-the-counter hearing aids, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Hearing Aid Improvement Act of 2026 .\n#### 2. Demonstration project on coverage by Department of Veterans Affairs of over-the-counter hearing aids\n##### (a) Establishment of demonstration project\nBeginning not later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs (in this section referred to as the Secretary ) shall commence a project (in this section referred to as the demonstration project ) to demonstrate and evaluate the fiscal impact of covering FDA-cleared, over-the-counter hearing aids under section 1707(b) of title 38, United States Code, in the same or similar manner as coverage is provided for prescription hearing aids under such section.\n##### (b) Duration\nThe Secretary shall carry out the demonstration project for a period of two years.\n##### (c) Eligible participants\nA veteran is eligible to participate in the demonstration project if\u2014\n**(1)**\nthe veteran is enrolled in the system of annual patient enrollment established and operated under section 1705(a) of title 38, United States Code;\n**(2)**\nan audiologist determines, through a clinical evaluation of the veteran, that\u2014\n**(A)**\nfurnishing an over-the-counter hearing aid to the veteran for mild-to-moderate hearing loss is medically necessary;\n**(B)**\nthe veteran has no red flag conditions or contraindications for over-the-counter hearing aid use, as specified by the Food and Drug Administration; and\n**(3)**\nthe veteran has access to a mobile phone device and mobile data or Wi-Fi, or any successor technology, to operate over-the-counter hearing aid functionality.\n##### (d) Locations\nThe Secretary shall carry out the demonstration project at not fewer than two medical facilities of the Department of Veterans Affairs selected by the Secretary across different Veterans Integrated Services Networks and that have a demonstrated ability to reduce access barriers and provide services to a diverse veteran population in both rural and urban settings and surrounding areas.\n##### (e) Project design\n**(1) In general**\nThe Secretary shall design the demonstration project to demonstrate the effectiveness of FDA-cleared, over-the-counter hearing aids compared to professionally fitted prescription hearing aids by an audiologist according to the audiological best practices of the Department of Veterans of Affairs, including the fiscal impact on the Department of providing permanent coverage of over-the-counter hearing aids under section 1707(b) of title 38, United States Code.\n**(2) Design elements**\n**(A) In general**\nThe Secretary shall ensure the demonstration project includes the following study groups:\n**(i)**\nAn FDA-cleared, over the counter hearing aid group.\n**(ii)**\nAn audiologist-fitted prescription hearing aid group.\n**(B) Participants**\nThe Secretary shall allocate an approximately equal number of participants in the demonstration project to each group specified in subparagraph (A).\n##### (f) Measurement of benefits\nTo the maximum extent possible, in carrying out the demonstration project, the Secretary shall measure both self-reported benefits and speech recognition in noise among a diverse veteran population and evaluate the fiscal impact over a two-year follow-up period of permanent coverage of over-the-counter hearing aids under section 1707(b) of title 38, United States Code, for the FDA-cleared, over-the-counter hearing aids found under the demonstration project to be most beneficial.\n##### (g) Consultation\nIn conducting the demonstration project, the Secretary shall consult with organizations that represent consumers with mild-to-moderate hearing loss and other stakeholder organizations.\n##### (h) Reports\n**(1) Interim report**\nNot later than one year after the commencement of the demonstration project, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report that describes the progress and preliminary findings from the demonstration project.\n**(2) Final report**\n**(A) In general**\nNot later than 180 days after the last day of the demonstration project and after solicitation and consideration of formal written input on the project from organizations specified under subsection (g), the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a final report on the project.\n**(B) Elements**\nThe report required under subparagraph (A) shall include an evaluation of the fiscal impact on the Department of Veterans Affairs of providing permanent coverage of over-the-counter hearing aids under section 1707(b) of title 38, United States Code, and such other findings and recommendations as the Secretary determines appropriate.\n##### (i) FDA-Cleared, over-The-Counter hearing aid defined\nIn this section, the term FDA-cleared, over-the-counter hearing aid means a device\u2014\n**(1)**\ncleared by the Food and Drug Administration;\n**(2)**\nfully regulated by the Food and Drug Administration under section 520(q) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360j(q) ); and\n**(3)**\nthat contains features that allow personalization through technology, such as hearing tests, software, and smart phone applications.\n#### 3. Comptroller General study and report on veterans hearing aid benefits\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study on the furnishing to veterans with mild-to-moderate hearing loss under section 1707(b) of title 38, United States Code, of assistance for hearing aids and related examinations.\n##### (b) Elements\nThe study required under subsection (a)\u2014\n**(1)**\nshall include an examination of\u2014\n**(A)**\nthe number of individuals in the United States with mild-to-moderate hearing loss who need hearing aids;\n**(B)**\nthe medical coverage of such individuals relating to obtaining hearing aids; and\n**(C)**\nthe effectiveness of such medical coverage in meeting such need; and\n**(2)**\nmay include an examination of contract design for purchasing hearing aid devices.\n##### (c) Report\n**(1) In general**\nNot later than 18 months after the date of the enactment of this Act, the Comptroller General shall submit to Congress a report on the study conducted under subsection (a).\n**(2) Recommendations**\nThe report required under paragraph (1) shall include such recommendations on changes to programs and benefits of the Department of Veterans Affairs, including the establishment of new programs and benefits, as would meet the needs of veterans with mild-to-moderate hearing loss.",
      "versionDate": "2026-01-29",
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
        "updateDate": "2026-02-23T17:18:42Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3739is.xml"
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
      "title": "Veterans Hearing Aid Improvement Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Hearing Aid Improvement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to carry out a demonstration project on coverage by the Department of Veterans Affairs of over-the-counter hearing aids, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:35Z"
    }
  ]
}
```
