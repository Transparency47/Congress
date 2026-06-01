# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4590?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4590
- Title: KIDS Act
- Congress: 119
- Bill type: S
- Bill number: 4590
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-29T07:08:33Z
- Update date including text: 2026-05-29T07:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4590",
    "number": "4590",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "KIDS Act",
    "type": "S",
    "updateDate": "2026-05-29T07:08:33Z",
    "updateDateIncludingText": "2026-05-29T07:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T17:38:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4590is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4590\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Bennet introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo limit the Department of Homeland Security from detaining children and individuals with a cognitive disability and to prohibit immigration enforcement actions at sensitive locations without a court-issued criminal warrant.\n#### 1. Short titles\nThis Act may be cited as the Keeping Immigrants and Destinations Safe Act or the KIDS Act .\n#### 2. Definitions\nIn this Act:\n**(1) Child**\nThe term child has the meaning given such term in section 101(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1101(b)(1) ).\n**(2) Cognitive disability**\nThe term cognitive disability means a mental impairment that substantially limits one or more major life activities of an individual involving learning, reading, concentrating, thinking, or communicating, or the operation of a neurological or brain function, consistent with the meaning of disability under section 3(1) of the Americans with Disabilities Act ( 42 U.S.C. 12102(1) ).\n**(3) Department**\nThe term Department means the Department of Homeland Security.\n**(4) Primary caregiver**\nThe term primary caregiver means a noncitizen parent or legal guardian who is the primary caretaker of 1 or more minor children in the United States, including a noncitizen parent or legal guardian with a direct interest in family court, probate court, guardianship, or child welfare proceedings involving a minor child.\n**(5) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n**(6) Sensitive location**\nThe term sensitive location includes any physical space located within 1,000 feet of\u2014\n**(A)**\nany medical or mental health care facility, including any hospital, health care practitioner\u2019s office, accredited health clinic, vaccination or testing site, emergent or urgent care facility, or community health center;\n**(B)**\nany public or private school (including preschools, primary schools, secondary schools, and postsecondary schools (including colleges and universities)), any site of an early childhood education program, any other institution of learning, such as vocational or trade schools, and any other site where individuals who are unemployed or underemployed may apply for or receive workforce training;\n**(C)**\nany scholastic or education-related activity or event, including field trips and interscholastic events;\n**(D)**\nany school bus or school bus stop during periods when school children are present on the bus or at the stop;\n**(E)**\nany recreational facility for children, such as playgrounds and formal recreational facilities;\n**(F)**\nany child care focused facility, including child care centers, before or after school care centers, foster care facilities, and group homes for children;\n**(G)**\nany location where disaster or emergency response and relief is being provided by Federal, State, or local entities, such as\u2014\n**(i)**\nthe distribution of emergency supplies, food, and water;\n**(ii)**\nany place of temporary shelter;\n**(iii)**\nany place along an evacuation route; and\n**(iv)**\nany site where registration for disaster-related assistance or family reunification is taking place;\n**(H)**\nany location of any organization that\u2014\n**(i)**\nassists children, pregnant women, victims of crime or abuse, or individuals with significant mental or physical disabilities, including domestic violence shelters, child advocacy centers, facilities that serve disabled persons, drug or alcohol counseling and treatment facilities, rape crisis centers, supervised visitation centers, family justice centers, victims\u2019 services providers, and community-based organizations providing social services; or\n**(ii)**\nprovides disaster or emergency social services and assistance, or services for individuals experiencing homelessness, including food banks, pantries, or other establishments distributing food, and shelters;\n**(I)**\nany church, synagogue, mosque, or other place of worship or religious study, such as buildings rented for the purpose of religious services or a temporary facility or location where such activities are taking place;\n**(J)**\nany site of a funeral, graveside ceremony, wedding, or any site where other religious or civil ceremonies or observances are occurring;\n**(K)**\nany site during a public demonstration, such as a march, rally, or parade;\n**(L)**\nany Federal, State, or local courthouse, including immigration courts operated by the Executive Office for Immigration Review, the office of an individual\u2019s legal counsel or representative, probation offices, and any facility where programs or services are provided in relation to a court proceeding;\n**(M)**\nany congressional district office;\n**(N)**\nany office of the Social Security Administration;\n**(O)**\nany public assistance office, including locations at which individuals may apply for or receive unemployment compensation or report violations of labor and employment laws;\n**(P)**\nthe indoor or outdoor premises of a department of motor vehicles;\n**(Q)**\na polling place, including any building or infrastructure at which voting takes place during an election;\n**(R)**\na labor union hall or any other union-operated building or office at which registered applicants are referred in rotation to jobs;\n**(S)**\nany public library; or\n**(T)**\nany other location specified by the Secretary.\n#### 3. Detention of children\n##### (a) Limitation\nExcept as provided in section 5, the Department may not detain a child, an individual with a cognitive disability, or a primary caregiver of a child or individual with a cognitive disability.\n##### (b) Parental notice and reporting\nIf a detention is permitted under section 5, the Department may not detain any child or individual with a cognitive disability without the confirmed notification of a parent or legal guardian of such child or individual. All such detentions shall be reported to Congress not later than 24 hours after the Department takes such a child or individual into custody.\n##### (c) Limitation on detention of primary caregivers\nThere shall be a presumption that a primary caregiver of a child or an individual with a cognitive disability may not be detained unless the Department Secretary documents, based on clear and convincing evidence that has been provided to the primary caregiver of such child or individual, that release of the primary caregiver is unreasonable or impracticable.\n##### (d) Release to designated caregiver or child welfare authority\n**(1) In general**\nIf a child or an individual with a cognitive disability is detained by the Department in violation of subsection (a), the Department shall prioritize the prompt release of such child or individual to\u2014\n**(A)**\na parent or legal guardian;\n**(B)**\na designated caregiver identified by a parent or legal guardian of such child or individual;\n**(C)**\nthe appropriate State or local child or adult protective services agency; or\n**(D)**\nappropriate officials of the Department of Health and Human Services Office of Refugee Resettlement, if appropriate and practicable.\n**(2) Recognition of delegated parental authority**\nFor purposes of paragraph (1)(B), the Department shall recognize and give effect to any written instrument executed by a parent or legal guardian that delegates temporary caregiving authority or parental authority to another individual, including a power of attorney or other document authorized under applicable State law.\n**(3) Verification**\nThe Department may take reasonable steps to verify the identity of the designated caregiver or the authenticity of the written instrument described in paragraph (2), but such verification shall not unreasonably delay the release of the child or individual with a cognitive disability.\n**(4) Best interests of the child**\nAll determinations made under this subsection shall be guided by the best interests of the child or individual with a cognitive disability.\n#### 4. Limitation on enforcement actions at sensitive locations\n##### (a) In general\nExcept as provided in section 5, the Department may not conduct, engage in, or execute any immigration enforcement action that takes place at, is focused on, or occurs within 1,000 feet of, a sensitive location.\n##### (b) Travel to and from sensitive locations\nFor purposes of this section, an immigration enforcement action shall be considered to occur at a sensitive location if such action is taken while an individual is traveling to, attending, or returning from a sensitive location.\n#### 5. Exception for criminal warrants\nThe restrictions under sections 3 and 4 may not be construed to prohibit or restrict enforcement actions conducted pursuant to a criminal arrest warrant or a criminal search warrant issued by a court of competent jurisdiction.\n#### 6. Remedies for violations\nIn the event of a violation of section 4\u2014\n**(1)**\nany information obtained as a result of such enforcement action for purposes of establishing alienage or chargeability may not be\u2014\n**(A)**\nentered into the record or received into evidence in a removal proceeding; or\n**(B)**\nused by the Department to effectuate any type of removal;\n**(2)**\nthe noncitizen who was the subject of such removal proceedings may file a motion to enforce the prohibition under section 4, including through a motion to terminate such proceedings;\n**(3)**\nany individual who was detained in violation of such section shall be released from detention; and\n**(4)**\nany person wrongfully detained shall be placed in section 240 proceedings, which require the Department to rebut the presumption of the individual's eligibility for release by clear and convincing evidence.",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4590is.xml"
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
      "title": "KIDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:08:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "KIDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keeping Immigrants and Destinations Safe Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to limit the Department of Homeland Security from detaining children and individuals with a cognitive disability and to prohibit immigration enforcement actions at sensitive locations without a court-issued criminal warrant.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:03:39Z"
    }
  ]
}
```
