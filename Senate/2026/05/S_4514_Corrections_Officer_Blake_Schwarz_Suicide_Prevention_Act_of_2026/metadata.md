# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4514
- Title: Corrections Officer Blake Schwarz Suicide Prevention Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4514
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-29T16:28:37Z
- Update date including text: 2026-05-29T16:28:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4514",
    "number": "4514",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Corrections Officer Blake Schwarz Suicide Prevention Act of 2026",
    "type": "S",
    "updateDate": "2026-05-29T16:28:37Z",
    "updateDateIncludingText": "2026-05-29T16:28:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T20:07:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4514is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4514\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Ms. Duckworth introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide funding to the Bureau of Prisons, States, and localities to carry out mental health screenings and provide referrals to mental health care providers for certain corrections officers.\n#### 1. Short title\nThis Act may be cited as the Corrections Officer Blake Schwarz Suicide Prevention Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Advisory Board**\nThe term Advisory Board means the Advisory Board established pursuant to section 5(a).\n**(2) Corrections officer**\nThe term corrections officer means an officer or employee\u2014\n**(A)**\nof any detention facility, including a prison or jail, operated by, or under contract with, a Federal agency; and\n**(B)**\nthe job responsibilities of whom include providing for the custody of incarcerated individuals.\n**(3) Eligible detention center**\nThe term eligible detention center means\u2014\n**(A)**\nany prison or jail administered by the Bureau of Prisons or a State; and\n**(B)**\nany jail administered by a State or locality.\n**(4) Jail; prison**\nThe terms jail and prison have the meanings given those terms in section 10 of the Prison Rape Elimination Act of 2003 ( 34 U.S.C. 30309 ).\n**(5) Jail or prison administrator**\nThe term jail or prison administrator means an individual who has been appointed to a supervisory position in a Federal, State, or local jail or prison by the Federal Government, a State, or a locality.\n**(6) Law enforcement officer**\nThe term law enforcement officer means an officer of an entity administered by the Federal Government, a State, or locality that exists primarily to prevent and detect crime and enforce criminal laws.\n**(7) Locality**\nThe term locality means any city, county, township, town, borough, parish, village, or other general purpose political subdivision of a State.\n**(8) Mental health care center**\nThe term mental health care center means a facility, such as a hospital or private clinic, at which not less than 1 mental health care provider offers mental health services.\n**(9) Mental health care provider**\nThe term mental health care provider means\u2014\n**(A)**\na fully licensed professional or group of professionals who\u2014\n**(i)**\ndiagnoses mental health conditions;\n**(ii)**\nprovides mental health treatment; and\n**(iii)**\noperates near an eligible detention center; and\n**(B)**\nincludes a professional or group described in subparagraph (A) that provides mental health services at a hospital or private clinic.\n**(10) Mental health screening survey**\nThe term mental health screening survey means a mental health screening survey developed and administered by a State or locality pursuant to section 3(d)(1).\n**(11) Mental illness**\nThe term mental illness means a mental, behavioral, or emotional disorder that\u2014\n**(A)**\nresults in serious functional impairment; and\n**(B)**\nsubstantially interferes with or limits major life activities.\n**(12) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n#### 3. Grant program\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Attorney General shall establish a grant program to award grants to States and localities to\u2014\n**(1)**\nimplement and administer mental health screenings to corrections officers at eligible detention centers; and\n**(2)**\nas applicable, refer corrections officers described in paragraph (1) to mental health care providers.\n##### (b) Application\n**(1) In general**\nA State or locality seeking a grant under this section shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may reasonably require.\n**(2) Contents**\nA State or locality submitting an application under paragraph (1) shall include in the application\u2014\n**(A)**\na description of and a plan for the use of amounts from a grant under this section, as described in subsection (c); and\n**(B)**\nan assurance that the State or locality will hire a mental health liaison staff member to coordinate among\u2014\n**(i)**\neligible detention centers;\n**(ii)**\nmental health providers;\n**(iii)**\nthe Advisory Board; and\n**(iv)**\nthe outreach team of the State or locality established pursuant to subsection (e).\n##### (c) Eligible projects\nA State or locality receiving a grant under this section may use amounts from the grant only for the following:\n**(1)**\nTo develop and administer the mental health screening survey.\n**(2)**\nTo develop any technology necessary for an eligible detention center to provide the mental health screening survey.\n**(3)**\nTo hire any staff necessary for an eligible detention center to provide the mental health screening survey.\n**(4)**\nTo establish an outreach team pursuant to subsection (e).\n**(5)**\nTo pay the salaries or overtime pay of members of the mental health outreach team established pursuant to subsection (e), including by providing direct funding to an eligible detention center to compensate staff members of the mental health outreach team.\n##### (d) Brief mental health screening survey\n**(1) In general**\nA State or locality receiving a grant under this section shall develop or adopt a mental health screening survey, and administer a mental health screening survey, that\u2014\n**(A)**\nis for corrections officers of eligible detention centers;\n**(B)**\nmay be based on the questions and content of\u2014\n**(i)**\nthe standard mental health screening of the Employee Assistance Program of the Federal Bureau of Prisons; or\n**(ii)**\nthe initial mental health screening standard of the Bureau of Prisons;\n**(C)**\nseeks to identify mental illnesses, including schizophrenia, bipolar disorder, and major depression;\n**(D)**\nasks an individual about\u2014\n**(i)**\nthe symptoms of mental illness the individual may be experiencing or has experienced; and\n**(ii)**\nany prior use of mental health-related medications or inpatient care;\n**(E)**\nidentifies the place of residence of an individual;\n**(F)**\nis administered by a trained staff member at the applicable eligible detention center to all corrections officers; and\n**(G)**\nis anonymous and confidential.\n**(2) Referral**\n**(A) Notification**\nIf the responses of a correctional officer to the mental health screening survey indicate mental illness, the trained staff member administering the survey shall immediately notify the applicable mental health outreach team established pursuant to subsection (e).\n**(B) Action by outreach team**\nUpon receiving a notification of a correctional officer with a potential mental illness under subparagraph (A), the applicable mental health outreach team established pursuant to subsection (e) shall\u2014\n**(i)**\nrefer the correctional officer to a local mental health care provider for\u2014\n**(I)**\nfurther assessment and outreach; and\n**(II)**\nif necessary, admission to a mental health care center; and\n**(ii)**\nsupport the correctional officer in re-establishing ties with a mental health provider.\n##### (e) Outreach team\nA State or locality receiving a grant under this section shall establish a mental health outreach team composed of\u2014\n**(1)**\nmental health care providers;\n**(2)**\nif applicable, staff from an eligible detention center; and\n**(3)**\na mental health liaison staff member that oversees the mental health outreach team.\n#### 4. Bureau of prisons\nNot later than 90 days after the date of enactment of this Act, the Director of the Bureau of Prisons shall\u2014\n**(1)**\nestablish a program to develop and administer mental health surveys meeting the requirement of mental health screening surveys described in section 2(d)(1) to corrections officers of the Bureau of Prisons;\n**(2)**\nestablish and maintain an outreach team meeting the requirements of a mental health outreach team under section 2(e) to refer corrections officers to mental health care providers, as appropriate; and\n**(3)**\nsubmit to the Advisory Board a plan for the implementation of the program described in paragraph (1).\n#### 5. Advisory board on program implementation\n##### (a) Establishment\n**(1) In general**\nNot later than 60 days after the date of enactment of this Act, the Attorney General shall establish an Advisory Board to manage and administer the grant program under section 3.\n**(2) Duties**\nThe Advisory Board shall have responsibility for the following:\n**(A)**\nEvaluating and approving the plans submitted by a State or locality under section 3(b)(2)(A).\n**(B)**\nEnsuring that amounts from a grant under section 3 are used in accordance with section 3(c).\n**(C)**\nMonitoring plans submitted by the Bureau of Prisons in accordance with section 4(3) and advise the Attorney General on compliance to ensure that the Bureau of Prisons uses amounts appropriated to the Bureau of Prisons to carry out section 4.\n**(D)**\nProviding technical assistance to a State or locality to help with the implementation and administration of mental health screening and referral programs established by States and localities receiving a grant under section 3.\n**(E)**\nCreating a working group of mental health care providers, jail or prison administrators, law enforcement officers, and operators of existing mental health screening and referral programs to share best practices on how to create and implement mental health screening and referral programs that have the largest impact on reducing crime rates and improving employment and wage rates for individuals released from prison or jail.\n**(F)**\nWorking in coordination with mental health outreach teams established pursuant to section 3(e) to ensure that the grant program under section 3 operates in accordance with that section.\n**(G)**\nDetermining whether a State or locality receiving a grant under section 3 is not complying with the requirements of that section.\n**(H)**\nMandating necessary changes for States and localities not complying with the requirements of section 3 and reducing grant funding to those States and localities if the States and localities do not make those changes.\n##### (b) Technical assistance\nThe Advisory Board shall\u2014\n**(1)**\nprovide technical assistance to\u2014\n**(A)**\nthe States and localities receiving a grant under section 3 in carrying out the requirements of the grant; and\n**(B)**\nthe Director of the Bureau of Prisons in carrying out the requirements under section 4; and\n**(2)**\nidentify evidence-backed models for the administration of mental health screening and referral programs that the Bureau of Prisons, States, and localities can look to when designing their own programs.\n##### (c) Membership\n**(1) In general**\nThe Attorney General shall appoint members to serve on the Advisory Board who have expertise in\u2014\n**(A)**\ndesigning and administering employee mental health screenings and providing mental health referrals for employees;\n**(B)**\nmental health care within prisons or jails; or\n**(C)**\nmental health program evaluation using rigorous experimental and quasi-experimental statistical methods.\n**(2) Number of members**\nThe Attorney General\u2014\n**(A)**\nshall appoint to the Advisory Board not less than 3 members; and\n**(B)**\nin addition to the members required under subparagraph (A), may appoint to the Advisory Board as many members as the Attorney General determines appropriate.\n#### 6. Safe harbor\nA State or locality receiving a grant under section 3 and the Director of the Bureau of Prisons shall ensure that, with respect to a corrections officer experiencing a mental health issue, the corrections officer\u2014\n**(1)**\ndoes not suffer an adverse employment outcome, including a fitness for duty evaluation as a result of the mental health issue while the corrections officer is seeking and receiving treatment for the mental health issue; and\n**(2)**\ndetermines the proper course of treatment in conjunction with the mental health care provider of the of the corrections officer.\n#### 7. Funding\n##### (a) Authorization\nThere is authorized to be appropriated to the Attorney General to carry out this Act\u2014\n**(1)**\n$50,000,000 for fiscal year 2026;\n**(2)**\n$55,000,000 for fiscal year 2027;\n**(3)**\n$60,000,000 for fiscal year 2028;\n**(4)**\n$65,000,000 for fiscal year 2029; and\n**(5)**\n$70,000,000 for fiscal year 2030.\n##### (b) Distribution of funds\nOf the amounts made available pursuant to subsection (a), the Attorney General shall use\u2014\n**(1)**\n90 percent to carry out sections 3 and 4, of which\u2014\n**(A)**\n20 percent shall be for the Director of the Bureau of Prisons to carry out section 4;\n**(B)**\n20 percent shall be for grants to States under section 3; and\n**(C)**\n50 percent shall be for grants to localities under section 3;\n**(2)**\n5 percent for the Advisory Board to carry out section 5(a)(2); and\n**(3)**\n5 percent for the Advisory Board to carry out section 5(b).",
      "versionDate": "2026-05-13",
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
        "updateDate": "2026-05-29T16:28:37Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4514is.xml"
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
      "title": "Corrections Officer Blake Schwarz Suicide Prevention Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Corrections Officer Blake Schwarz Suicide Prevention Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide funding to the Bureau of Prisons, States, and localities to carry out mental health screenings and provide referrals to mental health care providers for certain corrections officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:43Z"
    }
  ]
}
```
