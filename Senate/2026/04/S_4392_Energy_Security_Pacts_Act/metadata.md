# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4392
- Title: Energy Security Pacts Act
- Congress: 119
- Bill type: S
- Bill number: 4392
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-28T20:46:18Z
- Update date including text: 2026-05-28T20:46:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4392",
    "number": "4392",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Energy Security Pacts Act",
    "type": "S",
    "updateDate": "2026-05-28T20:46:18Z",
    "updateDateIncludingText": "2026-05-28T20:46:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T21:35:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NE"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CO"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4392is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4392\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Coons (for himself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo promote United States and allied energy and mineral security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Security Pacts Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations, the Committee on Finance, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs, the Committee on Ways and Means, and the Committee on Appropriations of the House of Representatives.\n**(2) Council agency**\nThe term council agency means a department, agency, or organization described in section 6(c).\n**(3) Critical mineral**\nThe term critical mineral means any mineral on the list of critical minerals required by section 7002(c)(3) of the Energy Act of 2020 ( 30 U.S.C. 1606(c)(3) ) on or after January 1, 2026.\n**(4) Director for Energy Security Pacts**\nThe term Director for Energy Security Pacts means the Director for Energy Security Pacts described in section 4.\n**(5) Energy Security Pact**\nThe term Energy Security Pact means an Energy Security Pact described in section 3.\n**(6) Energy Security Pacts Council**\nThe term Energy Security Pacts Council means the Energy Security Pacts Council established under section 6.\n**(7) Partner country**\nThe term partner country means a country eligible for participation in an Energy Security Pact.\n**(8) Secretary**\nThe term Secretary means the Secretary of State.\n**(9) Under Secretary**\nThe term Under Secretary means the Under Secretary of State for Economic Growth, Energy, and the Environment.\n#### 3. Authority and funding for Energy Security Pacts\n##### (a) In general\nThe Secretary may establish multiyear agreements (to be known as Energy Security Pacts ) with partner countries under which the Secretary may coordinate and provide assistance to enhance the energy and economic security and stability of the United States and such partner countries, including through efforts to counter economic coercion through the diversification of critical mineral and energy supply chains.\n##### (b) Funding\n**(1) Availability of amounts**\nThe Secretary may make available, from amounts authorized to be appropriated for fiscal year 2026 or any subsequent fiscal year under the heading National Security Investment Programs in Acts making appropriations for the Department of State, foreign operations, and related programs (including amounts authorized to be appropriated to the Economic Resilience Initiative), amounts for the purpose of establishing and implementing Energy Security Pacts.\n**(2) Transfers**\nFunds authorized to be made available pursuant to paragraph (1) may be transferred to, and merged with, funds appropriated for fiscal year 2026 or any subsequent fiscal year under the headings United States Trade and Development Agency , Millennium Challenge Corporation , United States International Development Finance\u2013Corporate Capital Account , United States International Development Finance\u2013Program Account , Development Finance Corporate Equity Investment Account , and Export-Import Bank of the United States\u2013Program Account to carry out the purpose described in paragraph (1).\n**(3) Consultation and notification**\nThe transfer authority provided by this subsection is\u2014\n**(A)**\nin addition to any other transfer authority provided by law; and\n**(B)**\nsubject to\u2014\n**(i)**\nprior consultation with\u2014\n**(I)**\nthe Committee on Appropriations and the Committee on Foreign Relations of the Senate; and\n**(II)**\nthe Committee on Appropriations and the Committee on Foreign Affairs of the House of Representatives; and\n**(ii)**\nthe regular notification procedures of such committees.\n##### (c) Assistance for the development and implementation of Pacts\nThe Director for Energy Security Pacts may\u2014\n**(1)**\nenter into contracts for required technical support related to Energy Security Pacts;\n**(2)**\nmake grants to partner countries that meet eligibility requirements for United States foreign assistance for the purpose of building the administrative or technical capacity necessary to facilitate the development and implementation of an Energy Security Pact between the United States and such country; and\n**(3)**\nlead Country Pact Teams, in accordance with section 4(c), to carry out the implementation of Energy Security Pacts.\n##### (d) Limitations\n**(1) Prohibition on military assistance and training**\nAssistance under this section may not include military assistance or military training for a country.\n**(2) Prohibition on assistance relating to united states job loss or production displacement**\nAssistance under this section may not be provided for any project that is likely to cause a substantial loss of United States jobs or a substantial displacement of United States production.\n**(3) Prohibition on assistance relating to environmental, health, or safety hazards**\nAssistance under this section may not be provided for any project that is likely to cause a significant environmental, health, or safety hazard.\n**(4) Foreign Aid Transparency and Accountability Act compliance**\nNone of the funds authorized to be appropriated or otherwise made available to carry out this Act may be obligated or expended for an Energy Security Pact unless the Secretary complies with the requirements of section 4 of the Foreign Aid Transparency and Accountability Act of 2016 ( 22 U.S.C. 2394c ) with respect to the Pact and all activities associated with the Pact.\n**(5) Prohibition on assistance for certain entities**\nNone of the funds authorized to be appropriated or otherwise made available to carry out this Act may be obligated or expended to provide any grant, contract, loan, or other financial assistance to an entity in which a senior United States Government official or an immediate family member (as defined in section 1128(j) of the Social Security Act ( 42 U.S.C. 1320a\u20137(j) )) of such official holds any ownership interest or serves in any managerial, officer, director, or board capacity.\n**(6) Other prohibition**\nAssistance under this section may not be used in any manner otherwise prohibited by any provision of law.\n#### 4. Office of Energy Security Pacts\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall establish an Office of Energy Security Pacts, which shall perform such functions related to the administration, coordination, and implementation of Energy Security Pacts as the Under Secretary may prescribe.\n##### (b) Director for Energy Security Pacts\n**(1) In general**\nThe Office of Energy Security shall be led by a Director for Energy Security Pacts, who shall be\u2014\n**(A)**\nappointed by the Secretary; and\n**(B)**\nresponsible\u2014\n**(i)**\nto the Under Secretary for all matters pertaining to the administration and implementation of Energy Security Pacts; and\n**(ii)**\nfor such other related duties as the Secretary may from time to time designate.\n**(2) Responsibilities**\nIn addition to the responsibilities described in paragraph (1), the Director for Energy Security Pacts shall be responsible for supporting the coordination and implementation by the Department of State of the Economic Resilience Initiative and the Energy Security Pacts Council, including for all matters pertaining to the following:\n**(A)**\nDrafting the contribution of the Secretary to the strategy required by section 7030(d) of the Further Consolidated Appropriations Act, 2024 ( Public Law 118\u201347 ; 138 Stat. 782).\n**(B)**\nLeading the development, negotiation, and management of all Energy Security Pacts.\n**(C)**\nConsulting and coordinating with council agencies to develop prospective Energy Security Pacts and implement ongoing Energy Security Pacts, as appropriate.\n**(D)**\nServing as the recipient for\u2014\n**(i)**\nsolicited proposals under Energy Security Pacts; and\n**(ii)**\nunsolicited proposals for projects to be considered for inclusion in any Energy Security Pact by national, regional, and local governments and private corporations.\n**(E)**\nSigning joint agency agreements on behalf of the Department of State, transferring or receiving appropriated funds from any department, agency, or independent establishment of the United States Government on behalf of the Department of State (with the consent of the head of such department, agency, or establishment) for the purpose of developing, implementing, or otherwise participating in an Energy Security Pact, including for use as a credit subsidy to provide loans.\n**(F)**\nCoordinating with other donor entities, including countries that are allies and partners of the United States, the Forum on Resource Geostrategic Engagement of the Department of State, and other multilateral fora, for purposes of deconflicting, augmenting, and leveraging, as appropriate, Energy Security Pact workplans with the development and financing activities performed by others.\n**(3) Annual report required**\nNot less frequently than annually until the date that is 5 years after the date of the enactment of this Act, the Director for Energy Security Pacts shall submit to the appropriate congressional committees, the Executive Office of the President, the National Security Council, and the Secretary a report describing\u2014\n**(A)**\nthe current status of activities authorized under this Act;\n**(B)**\nany obstacles to the implementation of such activities; and\n**(C)**\nany updates to the multiyear financial plan developed pursuant to section 5(d)(G).\n##### (c) Country Pact Teams\n**(1) In general**\nThe Secretary, in consultation with the Under Secretary and relevant Federal departments and agencies, shall designate a Country Pact Team for each Energy Security Pact.\n**(2) Leadership; duties**\nEach Country Pact Team shall\u2014\n**(A)**\nbe led by the Director for Energy Security Pacts, who shall regularly engage with the Energy Security Pacts Council on matters related to the Energy Security Pact; and\n**(B)**\nmanage the day-to-day activities related to the development, negotiation, implementation, and monitoring of the Pact.\n##### (d) Personnel\n**(1) In general**\nThe Under Secretary or the Under Secretary\u2019s designee may\u2014\n**(A)**\ndetail staff to heads of council agencies with relevant sectoral, financial, or regional expertise for the express purpose of supporting the negotiation or implementation of an Energy Security Pact;\n**(B)**\nrequest from the heads of council agencies the detail of personnel to the Office of Energy Security Pacts with relevant sectoral, financial, or regional expertise, on a reimbursable basis, for the express purpose of supporting the negotiation or implementation of an Energy Security Pact; and\n**(C)**\nappoint, without regard to the provisions of sections 3309 through 3318 of title 5, United States Code, candidates directly to positions in the competitive service, as defined in section 2102 of that title.\n**(2) Detailed employees**\nAny employee detailed pursuant to a request made under paragraph (1)(B) shall remain, for the purpose of preserving such employee\u2019s allowances, privileges, rights, seniority, and other benefits, an employee of the agency from which detailed.\n##### (e) Termination\n**(1) New Energy Security Pacts**\nThe authority to enter into new Energy Security Pacts shall terminate on the date that is 15 years after the date of the enactment of this Act.\n**(2) Office; Director; Council**\nThe Office of Energy Security Pacts, the position of Director for Energy Security Pacts, and the Energy Security Pacts Council shall terminate after the final Energy Security Pact expires.\n##### (f) Reports\nNot later than 180 days after the date of the enactment of this Act, the Under Secretary shall submit to the appropriate congressional committees a report that contains plans to attract and retain diplomatic, policy, legal, and technical expertise for civil service officers in the Office of Energy Security Pacts, including career promotion tracks to supervisory and non-supervisory GS\u201315 positions.\n#### 5. Approval, eligibility, and elements of Energy Security Pacts\n##### (a) Goal\nIt shall be the goal of each Energy Security Pact to increase reliable access to energy or electricity, including that needed for production of critical minerals, for the United States and the partner country to the Energy Security Pact, for the purpose of stimulating economic growth, enabling follow-on private sector investment, supporting the commercial competitiveness of United States companies, or diversifying relevant supply chains.\n##### (b) Initial requirements\n**(1) Recommendation; analysis**\nBefore entering into an Energy Security Pact\u2014\n**(A)**\nthe Pact shall be recommended by the Director for Energy Security Pacts and the Under Secretary and approved by the Secretary; and\n**(B)**\nthe Director for Energy Security Pacts, in collaboration with the Energy Security Pacts Council and partner country, shall conduct a constraints analysis that identifies insufficiencies in the energy sector and supply-chain segments needed to strengthen the partner country\u2019s energy security, consistent with United States energy security risks and commercial opportunities.\n**(2) Congressional notification**\nNot later than 30 days before entering into an Energy Security Pact, the Director for Energy Security Pacts shall\u2014\n**(A)**\nnotify and consult with the appropriate congressional committees regarding such Pact;\n**(B)**\ntransmit to the appropriate congressional committees the text of such Pact; and\n**(C)**\nprovide to the appropriate congressional committees an in-person briefing regarding such Pact.\n##### (c) Eligibility\nA country is eligible for participation in an Energy Security Pact if\u2014\n**(1)(A)**\nthe per capita income of the country is not greater than the World Bank's loan threshold; or\n**(B)**\nat the beginning of the year in which negotiations are initiated, the country is eligible for support from the World Bank's International Bank for Reconstruction and Development or International Development Association graduation process;\n**(2)**\nthe country has been identified as strategically or commercially important for the United States by the Secretary or the President;\n**(3)**\nthe Under Secretary determines that the country has the capacity and commitment to implement the Energy Security Pact; and\n**(4)**\nthe country is not a foreign country of concern (as defined in section 10612(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19221(a) )).\n##### (d) Energy Security Pact elements\n**(1) In general**\nEach Energy Security Pact shall contain the following:\n**(A)**\nThe constraints analysis conducted under subsection (b)(1)(B).\n**(B)**\nA demonstrated effort to integrate the national economic development strategy of the partner country.\n**(C)**\nSpecific objectives that the partner country and the United States expect to achieve during the term of the Energy Security Pact, including\u2014\n**(i)**\nincreased energy production, reliability, and affordability in the partner country;\n**(ii)**\neconomic growth in the partner country that may reduce the need for foreign assistance;\n**(iii)**\nimproved access to energy, in consultation with affected communities and civil society; and\n**(iv)**\nimproved infrastructure that enables access to critical minerals mining and processing.\n**(D)**\nThe responsibilities of the partner country and the United States in the achievement of such objectives.\n**(E)**\nRegular quantitative benchmarks to measure, as appropriate, progress toward achieving such objectives.\n**(F)**\nAn identification of the intended impact of the activities carried out in accordance with the Energy Security Pact.\n**(G)**\nA multiyear financial plan, updated annually until the expiration of the term of the Energy Security Pact, that\u2014\n**(i)**\nestimates the amount of contributions, commitments, and other participation to be provided by council agencies, the partner country, multilateral development banks, and other development finance institutions as applicable;\n**(ii)**\nensures that the Pact incorporates and is complementary to development programs administered by other Federal departments and agencies, so that United States funds are used to improve feasibility for private sector investment to further development goals;\n**(iii)**\nidentifies proposed mechanisms to implement the plan and provide oversight of the plan; and\n**(iv)**\ndescribes how the requirements described in this subsection will be met, including the role of the private sector in the achievement of such requirements.\n**(H)**\nAs appropriate, a description of the current and potential participation of other donors, including council agencies or countries that are allies and partners of the United States, in the achievement of the objectives described in subparagraph (C).\n**(I)**\nA description of how oversight and transparency of the foreign assistance provided through the Economic Resilience Initiative will be maintained.\n**(J)**\nAs appropriate, a process or processes for considering\u2014\n**(i)**\nsolicited proposals under the Energy Security Pact; and\n**(ii)**\nunsolicited proposals by national, regional, and local governments and private corporations.\n**(K)**\nA requirement that open, fair, competitive, and transparent procedures are used in the administration of grants or cooperative agreements or the procurement of goods and services for the accomplishment of objectives under the Energy Security Pact.\n**(L)**\nThe strategy of the partner country to sustain progress made toward achieving the objectives described in subparagraph (C) after expiration of the Energy Security Pact.\n**(M)**\nA description of the role of council agencies in any design, implementation, and monitoring of programs and activities funded through the Energy Security Pact.\n**(N)**\nA description of any contribution, as appropriate, from the partner country relative to its national budget and taking into account the prevailing economic conditions, toward meeting the objectives described in subparagraph (C).\n**(2) Prohibition on taxation**\nIn addition to the elements described in paragraph (1), each Energy Security Pact shall contain a provision stating that assistance provided by the United States under the Energy Security Pact shall be exempt from taxation by the government of the partner country.\n**(3) Energy sources**\nAn Energy Security Pact shall not exclude, as a matter of policy, any specific type of energy or power generation.\n##### (e) Notification regarding increase or extension of assistance\nNot later than 15 days after making a determination and before distributing funds to increase or extend assistance under an Energy Security Pact with a partner country, the Secretary, acting through the Director for Energy Security Pacts, shall submit to the appropriate congressional committees a written notification that contains the following:\n**(1)**\nA justification for the determination.\n**(2)**\nA detailed summary of the proposed increase in, or extension of, assistance under the Energy Security Pact.\n**(3)**\nA copy of the full text of the amendment to the Energy Security Pact.\n##### (f) Duration\nThe duration of an Energy Security Pact may not exceed 10 years.\n##### (g) Subsequent and concurrent pacts\nA partner country that has entered into, and has in effect, an Energy Security Pact may enter into, and concurrently have in effect, additional Energy Security Pacts.\n##### (h) Rule of construction\nNothing in this section shall be construed to alter, supersede, or otherwise affect any authorities, restrictions, or eligibility requirements existing on the date of the enactment of this Act applicable to foreign assistance programs administered by any Federal department or agency, including determinations regarding the eligibility of countries for such assistance made pursuant to the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) or any other provision of law.\n#### 6. Energy Security Pacts Council\n##### (a) Establishment\nNot later than 90 days after the date of the enactment of this Act, the President shall establish an Energy Security Pacts Council (in this section referred to as the Council ) to coordinate and implement Energy Security Pacts.\n##### (b) Chairperson\nThe Council shall be chaired by the Secretary.\n##### (c) Composition\nThe Council shall be composed of principal officers of executive departments from the following:\n**(1)**\nThe United States International Development Finance Corporation.\n**(2)**\nThe Department of Energy.\n**(3)**\nThe United States Trade and Development Agency.\n**(4)**\nThe Export-Import Bank of the United States.\n**(5)**\nThe Department of Commerce.\n**(6)**\nThe United States Trade Representative.\n**(7)**\nThe Department of Defense.\n**(8)**\nThe Department of State.\n**(9)**\nThe Department of the Treasury.\n**(10)**\nThe Millennium Challenge Corporation.\n**(11)**\nThe Department of the Interior.\n**(12)**\nAny other Federal department, agency, or organization that the President determines to be appropriate.\n##### (d) Vacancies\nWhen there is a vacancy in the office of a principal officer of an executive department, the individual acting in the capacity of principal officer shall serve as a member of the Council until a new principal officer of the executive department is appointed.\n##### (e) Delegation\nThe principal officer of an executive department may delegate a senior official (as described in section 1(d) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(d) ) or following other relevant agency guidance) to serve on the Council, as appropriate.\n##### (f) Meetings\nThe Council shall meet not less frequently than quarterly.\n##### (g) Duties\nThe Council shall\u2014\n**(1)**\ncoordinate Energy Security Pact-related activities of the council agencies;\n**(2)**\nmake annual recommendations to the Director for Energy Security Pacts, taking into account the stated priorities of the National Security Council and the President, regarding the prioritization of countries eligible for Energy Security Pact negotiation; and\n**(3)**\nmake recommendations to improve interagency collaboration for purposes of promoting energy security and United States national security interests abroad.\n##### (h) Sunshine Act compliance\nMeetings of the Council are subject to section 552b of title 5, United States Code (commonly referred to as the Government in the Sunshine Act ).\n#### 7. Evaluation by Government Accountability Office\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter until the final Energy Security Pact expires, the Comptroller General of the United States shall submit to Congress an evaluation of the efficiency and development impact of projects supported by an Energy Security Pact.",
      "versionDate": "2026-04-27",
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
        "name": "International Affairs",
        "updateDate": "2026-05-28T20:46:17Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4392is.xml"
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
      "title": "Energy Security Pacts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T10:58:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Energy Security Pacts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote United States and allied energy and mineral security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:03:25Z"
    }
  ]
}
```
