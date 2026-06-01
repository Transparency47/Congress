# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/666?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/666
- Title: First Responders Wellness Act
- Congress: 119
- Bill type: S
- Bill number: 666
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-08-06T19:32:17Z
- Update date including text: 2025-08-06T19:32:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/666",
    "number": "666",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "First Responders Wellness Act",
    "type": "S",
    "updateDate": "2025-08-06T19:32:17Z",
    "updateDateIncludingText": "2025-08-06T19:32:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T18:36:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s666is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 666\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mrs. Gillibrand (for herself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo increase access to mental health, substance use, and counseling services for first responders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the First Responders Wellness Act .\n#### 2. First responders mental health hotline\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. First responders mental health hotline (a) In general Not later than 2 years after the date of enactment of the First Responders Wellness Act , the Secretary, acting through the Assistant Secretary for Mental Health and Substance Use, shall maintain, directly or by contract or grant, a national first responders emergency hotline to provide peer and emotional support, information, brief intervention, and mental and behavioral health and substance use disorder resources and referrals to first responders and to their families or household members. (b) Requirements for hotline The hotline established under subsection (a) shall\u2014 (1) operate as a separate, widely recognizable number with bidirectional transfer options with the 988 Suicide and Crisis Lifeline established pursuant to section 520E\u20133; (2) provide toll-free, real-time, live assistance 24/7; (3) provide voice and text support; (4) be sufficiently staffed by, at a minimum, culturally competent first responder peer specialists or first responder mental health services providers who have distinct knowledge of, and are trained on\u2014 (A) the essential functions of first responders and public safety organizations; (B) the working conditions unique to first responders; (C) common and novel stressors inherent in public safety and emergency response work; (D) normal and abnormal adaptation to occupational stress and trauma; and (E) the unique aspects of confidentiality and testimonial privilege; and (5) provide peer support, mental and behavioral health and substance use disorder assistance, and referral services to meet the needs of first responders and family members or household members at risk of experiencing mental or behavioral health or substance use disorders. (c) Additional requirements (1) In general In maintaining the hotline under subsection (a), the Secretary shall\u2014 (A) consult with the National Domestic Violence Hotline, the 988 Suicide and Crisis Lifeline, and the Veterans Crisis Line to ensure that first responders are connected in real-time to the appropriate specialized hotline service, when applicable; (B) conduct a public awareness campaign for the hotline under subsection (a); (C) consult with Federal departments and agencies, including the Substance Abuse and Mental Health Services Administration and the Department of Justice, to increase awareness regarding the hotline under subsection (a); and (D) consult with organizations that operate existing crisis or peer support hotlines for first responders with respect to best practices for operating such hotlines. (2) Existing hotlines The Secretary or an entity receiving a grant or contract under subsection (a), as applicable, shall form partnerships between the existing national first responders mental health hotline and other first responder helplines and websites. (3) Coordination The Secretary shall ensure that calls from public safety personnel received through the 988 Suicide and Crisis Lifeline are appropriately referred to the hotline under subsection (a). (4) Training curriculum Not later than 2 years after the date of enactment of the First Responders Wellness Act , the Secretary shall develop, in coordination with mental health providers and first responder associations or personnel, trauma-informed and culturally competent training, guidance, and standards for 988 Suicide and Crisis Lifeline network center personnel on the unique concerns, resources, linkages, and stressors of first responders. (d) Annual report The Secretary shall submit an annual report to Congress on the hotline under subsection (a) and implementation of this section, including\u2014 (1) an evaluation of the effectiveness of activities conducted or supported under subsection (a); (2) an evaluation of staffing levels necessary to maintain adequate services; (3) a directory of entities or organizations to which staff maintaining the hotline funded under this section may make referrals; and (4) such additional information as the Secretary determines appropriate. (e) Definitions In this section: (1) Culturally competent first responder peer specialist The term culturally competent first responder peer specialist means an individual\u2014 (A) with familiarity with, and understanding of, the duties and unique stressors of first responders, which may include experience working as a first responder; and (B) who completed a trauma-informed and culturally competent training curriculum developed pursuant to subsection (c)(4), or another trauma-informed and culturally competent training curriculum, as the Secretary determines appropriate. (2) First responder The term first responder \u2014 (A) means\u2014 (i) a law enforcement officer, firefighter, or member of a rescue squad or ambulance crew (as such terms are defined in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968); or (ii) a public safety telecommunicator, including 9\u20131\u20131 operators and dispatchers; and (B) includes a retired first responder. (3) First responder mental health services provider The term first responder mental health services provider includes a State-licensed or State-certified counselor, trauma counselor, psychologist or other State licensed or certified mental health professional who\u2014 (A) is qualified under State law to provide mental or behavioral health services; and (B) has a familiarity with and understanding of the duties and unique stressors of first responders. (f) Authorization of appropriations To carry out this section, there are authorized to be appropriated $10,000,000 for each of fiscal years 2025 through 2031. .\n#### 3. Crisis counseling assistance and training\nSection 416(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5183(a) ) is amended by inserting and to qualified emergency response providers responding to major disasters after victims of major disasters .\n#### 4. Report on on-site services during a national disaster\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, shall issue a report on best practices and recommendations to establish a new mobile health care delivery site to provide integrated, short-term crisis services to qualified emergency response providers of a major disaster. Such services shall\u2014\n**(1)**\nbe culturally and linguistically appropriate;\n**(2)**\nbe trauma-informed; and\n**(3)**\nincorporate disaster behavioral interventions.\n##### (b) Definitions\nIn this section:\n**(1) Major disaster**\nThe term major disaster has the meaning given such term in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 ).\n**(2) Major disaster area**\nThe term major disaster area has the meaning given such term in section 625.2 of title 20, Code of Federal Regulations (or successor regulations).\n**(3) Qualified emergency response providers**\nThe term qualified emergency response providers means\u2014\n**(A)**\nemergency response providers (as defined in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 )); and\n**(B)**\npublic safety telecommunicators.",
      "versionDate": "2025-02-20",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-10T16:28:26Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-07-10T16:28:05Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-07-10T16:28:20Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-07-10T16:27:50Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-10T16:27:58Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-10T16:28:12Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-10T16:27:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-13T17:32:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
    "originChamber": "Senate",
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
          "measure-id": "id119s666",
          "measure-number": "666",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-08-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s666v00",
            "update-date": "2025-08-06"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>First Responders Wellness Act</strong></p><p>This bill establishes a national mental health hotline for first responders and provides mental health services for emergency response providers responding to major disasters.</p><p>The bill requires the Substance Abuse and Mental Health Services Administration (SAMHSA) to establish a mental health hotline staffed with specialists trained to provide first responders and their families with peer support, mental and behavioral health and substance use disorder assistance, and referral services. SAMHSA must raise awareness about the hotline and develop guidance regarding first responders for personnel operating the 988 Suicide and Crisis Lifeline. SAMHSA must report to Congress annually on the hotline.</p><p>Also, the bill expands the Crisis Counseling Assistance and Training Program, which provides mental health services to victims of major disasters, so that emergency response providers responding to major disasters may also receive these services.</p><p>Additionally, the bill requires\u00a0SAMHSA to publish a report with recommendations for establishing a mobile health care delivery site to provide crisis services to emergency response providers responding to a major disaster.</p>"
        },
        "title": "First Responders Wellness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s666.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>First Responders Wellness Act</strong></p><p>This bill establishes a national mental health hotline for first responders and provides mental health services for emergency response providers responding to major disasters.</p><p>The bill requires the Substance Abuse and Mental Health Services Administration (SAMHSA) to establish a mental health hotline staffed with specialists trained to provide first responders and their families with peer support, mental and behavioral health and substance use disorder assistance, and referral services. SAMHSA must raise awareness about the hotline and develop guidance regarding first responders for personnel operating the 988 Suicide and Crisis Lifeline. SAMHSA must report to Congress annually on the hotline.</p><p>Also, the bill expands the Crisis Counseling Assistance and Training Program, which provides mental health services to victims of major disasters, so that emergency response providers responding to major disasters may also receive these services.</p><p>Additionally, the bill requires\u00a0SAMHSA to publish a report with recommendations for establishing a mobile health care delivery site to provide crisis services to emergency response providers responding to a major disaster.</p>",
      "updateDate": "2025-08-06",
      "versionCode": "id119s666"
    },
    "title": "First Responders Wellness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>First Responders Wellness Act</strong></p><p>This bill establishes a national mental health hotline for first responders and provides mental health services for emergency response providers responding to major disasters.</p><p>The bill requires the Substance Abuse and Mental Health Services Administration (SAMHSA) to establish a mental health hotline staffed with specialists trained to provide first responders and their families with peer support, mental and behavioral health and substance use disorder assistance, and referral services. SAMHSA must raise awareness about the hotline and develop guidance regarding first responders for personnel operating the 988 Suicide and Crisis Lifeline. SAMHSA must report to Congress annually on the hotline.</p><p>Also, the bill expands the Crisis Counseling Assistance and Training Program, which provides mental health services to victims of major disasters, so that emergency response providers responding to major disasters may also receive these services.</p><p>Additionally, the bill requires\u00a0SAMHSA to publish a report with recommendations for establishing a mobile health care delivery site to provide crisis services to emergency response providers responding to a major disaster.</p>",
      "updateDate": "2025-08-06",
      "versionCode": "id119s666"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s666is.xml"
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
      "title": "First Responders Wellness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "First Responders Wellness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase access to mental health, substance use, and counseling services for first responders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:41Z"
    }
  ]
}
```
